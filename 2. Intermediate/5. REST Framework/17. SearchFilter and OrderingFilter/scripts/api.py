import requests

def run():
    response = requests.post(
        url="http://localhost:8000/products/create",
        data={
            "name": "Airpods Pro.",
            "description": "Black Metallic Component",
            "price": 33.99,
            "stock": 2
        },
        timeout=30
    )

    print(response.status_code)
    print(response.json())
