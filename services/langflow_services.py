import uuid
import os
import requests
from dotenv import load_dotenv


load_dotenv()

LANGFLOW_URL = os.environ.get("LANGFLOW_URL")
API_KEY = os.environ.get("LANGFLOW_API_KEY")


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
            "Prompt-AyzZR": {
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
    
    response.raise_for_status()

    data = response.json()

    return data
