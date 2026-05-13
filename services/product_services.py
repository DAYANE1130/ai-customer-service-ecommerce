import requests


# Listagem limitada de produtos com apenas as informações necessárias para o agente:

def fetch_products():
    try:
        api_res = requests.get(
            "https://dummyjson.com/products?limit=20").json()

        return api_res

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None


def get_products_for_ai():

        api_res = fetch_products()

        all_products = []

        if not api_res:
            return []

        for product in api_res['products']:

            all_products.append(
                {"title": product['title'],
                 "price": product['price'],
                 "rating": round(product['rating'])
                 }
            )

        return all_products