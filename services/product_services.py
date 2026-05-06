import requests

def call_api_products():
    try:
        api_res = requests.get("https://dummyjson.com/products?limit=20").json()

        # print(api_res)
        all_products = []

        for product in api_res['products']:

            all_products.append(
                {"title": product['title'],
                 "price": product['price'],
                 "rating": round(product['rating'])
                 }
            )
            
        return all_products
      
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return all_products

