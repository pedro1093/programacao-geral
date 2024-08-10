import requests
import asyncio

url = "https://script.google.com/macros/s/AKfycby8f4ZduJ6sUXAyGwFQS8a-WCTv97MU3H6fhWXeWLUYZOwHSz0JNGqlbhlY1wl6CKch/exec"

dados = {
    "action": "Create",
    "nome": "raspberry",
    "direita": "1",
    "esquerda": "0",
    "frente": "1",
    "re": "0",
}

async def adicionar_dados():
    params = dados
    request_url = f"{url}"
    
    try:
        response = requests.get(request_url, params=params)
        data = response.json()
        print("teste no servidor", data)
    except Exception as error:
        print("Erro ao adicionar dados ao servidor:", error)

async def fetch_data():
    url2 = "https://script.google.com/macros/s/AKfycby8f4ZduJ6sUXAyGwFQS8a-WCTv97MU3H6fhWXeWLUYZOwHSz0JNGqlbhlY1wl6CKch/exec"
    action = {'action': 'Read'}
    
    try:
        response = requests.get(url2, params=action)
        data = response.json()
        print('Dados da planilha:', data)
    except Exception as error:
        print('Erro ao buscar dados:', error)

async def main():
    await adicionar_dados()
    await fetch_data()

# Executar o código assíncrono
asyncio.run(main())
