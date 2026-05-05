from flask import Flask, render_template, request
import requests
import uuid
import os
from dotenv import load_dotenv
from database.customers import user_database
import json
import re

# Isso procura o arquivo .env e carrega as variáveis para o sistema
load_dotenv()

# Agora você acessa a variável normalmente
api_key = os.getenv("LANGFLOW_API_KEY")

app = Flask(__name__)

LANGFLOW_URL = os.environ.get("LANGFLOW_URL")
API_KEY = os.environ.get("LANGFLOW_API_KEY")





def call_langflow(question: str, user_info, product_list):
#def call_langflow(question: str, user_info):
    payload = {
        "input_type": "chat",
        "output_type": "chat",
        "input_value": question,
        "tweaks": {
            "Prompt-AyzZR": {
                "question": question,
                "user_info": str(user_info),
                "product_list":str(product_list)
            }
        },
        "session_id": str(uuid.uuid4())
    }

    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }

    response = requests.post(LANGFLOW_URL, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()

    # 👉 MVP: retorna bruto (depois a gente melhora)
    return data



@app.route('/', methods=['GET', 'POST'])
def home():
    user = user_database["8"]
    answer = "Olá, Dayane! Como posso ajudar você hoje?"
    produtos_recomendados = [] # Inicializa vazio para economizar tokens se não houver recomendação

    # 1. Busca produtos padrão da API (Plano B e suporte para Recomendações)
    try:
        api_res = requests.get("https://dummyjson.com/products?limit=20").json()
        all_products = [{"title": p['title'], "price": p['price'], "rating": round(p['rating'])} for p in api_res['products']]
    except:
        all_products = []

    intent_question = "Gere saudações e recomendações personalizadas."
    if request.method == 'POST':
        intent_question = request.form['question']

    try:
        # Chamada ao Langflow enviando o usuário e a lista de produtos (caso ela queira recomendar)
        raw_data = call_langflow(intent_question, user, all_products)
        ai_text = raw_data['outputs'][0]['outputs'][0]['results']['message']['text']
        
        # Extração do JSON
        match = re.search(r'\{.*\}', ai_text, re.DOTALL)
        if match:
            clean_json = json.loads(match.group(0))
            answer = clean_json.get("chat_answer")
            produtos_recomendados = clean_json.get("recommendations", [])
            
            # --- LÓGICA DE E-MAIL ---
            if clean_json.get("action_required") == "send_email":
                # Aqui você simula o envio usando os dados do Mock
                print(f"📧 [SISTEMA] Enviando e-mail para {user['email']}...")
                print(f"Conteúdo: Informações sobre os pedidos de {user['nome']}")
                answer += f" (Um e-mail com os detalhes foi enviado para {user['email']})"

        else:
            answer = ai_text # Fallback se a IA mandar só texto

    except Exception as e:
        print(f"Erro: {e}")
        answer = "Olá! Como posso ajudar?"
        produtos_recomendados = all_products[:3]

    return render_template('index.html', answer=answer, user=user, produtos=produtos_recomendados)

app.run(debug=True)
