from flask import Flask, render_template, request
from services.langflow_services import call_langflow
from services.product_services import get_products_for_ai
from database.customers import user_database
from services.email_services import send_email


app = Flask(__name__)


@app.route('/client/<int:id_client>', methods=['GET', 'POST'])
def home(id_client):
    user = user_database[str(id_client)]

    # Dados iniciais
    answer = f'Olá, {user["nome"]} Como posso ajudar você hoje?'
    recommended_products = []
    products = get_products_for_ai()

    try:
        # Fluxo do usuário envia pergunta sobre faq,recomendação ou pedidos:
        if request.method == "POST":
            question = request.form.get("question")

            if question:
                response = call_langflow(question, user, products)
                answer = response["chat_answer"]
                recommended_products = response["recommendations"]

                if response['action_required'] == "send_email":
                    send_email(
                        to_email=user["email"],
                        subject="Informações sobre pedido XXX",
                        body=response['email_body']
                    )

    except Exception as e:
        print(f"Erro: {e}")
        answer = "Desculpe, ocorreu um erro ao processar sua solicitação. Tente novamente em instantes."

    return render_template('index.html', answer=answer, user=user, products_list=recommended_products)


app.run(debug=True)
