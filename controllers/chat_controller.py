from services.langflow_services import call_langflow
from services.product_services import get_products_for_ai
from services.email_services import send_email


def process_user_message(question, user):
    products = get_products_for_ai()
    recommended_products = []

    try:
        products = get_products_for_ai()
        response = call_langflow(question, user, products)
        answer = response["chat_answer"]
        recommended_products = response["recommendations"]

        if response['action_required'] == "send_email":
            send_email(
                to_email=user["email"],
                subject="Informações de pedido",
                body=response['email_body']
            )

    except Exception as e:
        print(f"Erro DO CONTROLLER: {e}") #Degug de container flask
        answer = "Desculpe, ocorreu um erro ao processar sua solicitação. Tente novamente em instantes."

    return answer, recommended_products
