from flask import Flask, render_template, request
# import requests
import os
from services.langflow_services import call_langflow
from services.product_services import call_api_products
from database.customers import user_database

import json
import re


app = Flask(__name__)


@app.route('/client/<int:id_client>', methods=['GET', 'POST'])
def home(id_client):
    user = user_database[str(id_client)]

    # Dados iniciais
    answer = "Olá, Dayane! Como posso ajudar você hoje?"
    produtos_recomendados = []
    products = call_api_products()

    try:
        # Fluxo do usuário envia pergunta sobre faq ou pedidos:
        if request.method == 'POST':
            question = request.form.get('question')
            
            if question:
                response = call_langflow(question, user, products)
                print(response)

        # Fluxo que apenas exibe recomendações:
        else:
            response = call_langflow('', user, products)
            print(response)

    #     ai_text = raw_data['outputs'][0]['outputs'][0]['results']['message']['text']

    except Exception as e:
        print(f"Erro: {e}")
        answer = "Olá! Como posso ajudar?"
        produtos_recomendados = products[:3]

    return render_template('index.html', answer=answer, user=user, produtos=produtos_recomendados)


app.run(debug=True)
