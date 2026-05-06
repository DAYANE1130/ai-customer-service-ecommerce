from flask import Flask, render_template, request
import requests
import os
from services.langflow_services import call_langflow
from services.product_services import call_api_products
from database.customers import user_database

import json
import re


app = Flask(__name__)

@app.route('/client/<int:id_client>', methods=['GET', 'POST'])
def home(id_client):
    #id_client = request.args.get(id)
    print(id)
    
    user = user_database[str(id_client)]
    # Dados iniciais
    answer = "Olá, Dayane! Como posso ajudar você hoje?"
    produtos_recomendados = []

    # 1. Busca produtos padrão da API (Plano B e suporte para Recomendações)
  
    #products = call_api_products()
    # try:
    #     # Chamada ao Langflow enviando o usuário e a lista de produtos (caso ela queira recomendar)
    #     raw_data = call_langflow(intent_question, user, products)
    #     ai_text = raw_data['outputs'][0]['outputs'][0]['results']['message']['text']
        
       

    # except Exception as e:
    #     print(f"Erro: {e}")
    #     answer = "Olá! Como posso ajudar?"
    #     produtos_recomendados = products[:3]

    return render_template('index.html', answer=answer, user=user, produtos=produtos_recomendados)

app.run(debug=True)
