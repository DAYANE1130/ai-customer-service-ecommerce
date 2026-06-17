import uuid
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

LANGFLOW_URL = os.environ.get("LANGFLOW_URL")
API_KEY = os.environ.get("DOCKER_LANGFLOW_API_KEY")


def get_headers():
    return {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }


def build_payload(question, user_info, product_list):
    return {
        "input_type": "chat",
        "output_type": "chat",
        "input_value": question,
        "tweaks": {
            "Prompt-8UhDN": {
                "question": question,
                "user_info": str(user_info),
                "product_list": str(product_list)
            }
        },
        "session_id": str(uuid.uuid4())
    }


def call_langflow(question: str, user_info, product_list):
  
    payload = build_payload(question, user_info, product_list)
    
    headers = get_headers()
    
    response = requests.post(LANGFLOW_URL, json=payload, headers=headers)
    print("erro service langflow",response.status_code)
    print("erro service langflow",response.text)
    
    response.raise_for_status()

    data = response.json()

    
    text = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
    
    return json.loads(text)

# Testando formato de resposta
# response = {'chat_answer': 'Aceitamos diversas formas de pagamento, como Cartão de crédito, Pix e Boleto bancário. Para produtos de beleza, posso recomendar:', 
#  'recommendations': [{'title': 'Powder Canister', 'price': 14.99, 'rating': 5}, {'title': 'Red Lipstick', 'price': 12.99, 'rating': 4}, {'title': 'Red Nail Polish', 'price': 8.99, 'rating': 4}], 
#  'action_required': 'none', 'email_body': None}

# print(response['chat_answer'])

# for p in response["recommendations"]:
#     print(p['title'])