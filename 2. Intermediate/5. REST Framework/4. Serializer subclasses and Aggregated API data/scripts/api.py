import requests

def run():
    response = requests.post("http://localhost:8000/products", timeout=30)

    print(response.status_code)
    print(response.json())
