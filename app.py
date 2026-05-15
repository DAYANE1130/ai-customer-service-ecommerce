from flask import Flask, render_template, request
from database.customers import user_database
from controllers.chat_controller import process_user_message


app = Flask(__name__)


@app.route('/client/<int:id_client>', methods=['GET', 'POST'])
def home(id_client):
    user = user_database[str(id_client)]

    # Dados iniciais
    answer = f'Olá, {user["nome"]} Como posso ajudar você hoje?'
    recommended_products = []
  
    # Fluxo do usuário envia pergunta sobre faq,recomendação ou pedidos:
    if request.method == "POST":
        question = request.form.get("question")
        
        if question:
            answer, recommended_products = process_user_message(question, user)


    return render_template('index.html', answer=answer, user=user, products_list=recommended_products)


app.run(debug=True)
