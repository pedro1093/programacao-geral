import requests

def update_record(nome, direita=None, esquerda=None, frente=None, re=None):
    url = "https://script.google.com/macros/s/AKfycby8f4ZduJ6sUXAyGwFQS8a-WCTv97MU3H6fhWXeWLUYZOwHSz0JNGqlbhlY1wl6CKch/exec"
    
    params = {
        "action": "Update",
        "nome": nome,
        "direita": direita,
        "esquerda": esquerda,
        "frente": frente,
        "re": re
    }

    # Remove keys with None values
    params = {k: v for k, v in params.items() if v is not None}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        try:
            result = response.json()
            if result.get('status') == 'Sucesso':
                print("Registro atualizado com sucesso:", result.get('data'))
            else:
                print("Erro na atualização:", result.get('message'))
        except ValueError:
            print("Erro ao decodificar a resposta JSON")
    else:
        print("Erro:", response.status_code, response.text)

if __name__ == "__main__":
    # Exemplo de atualização
    update_record(nome="respiberry", direita=1, esquerda=0, frente=2, re=0)
