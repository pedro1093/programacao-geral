import requests

def read_records():
    url = "https://script.google.com/macros/s/AKfycbw6kmCN_N102CkrnK-sg_lOOsWDgcTFjzeox0s4hkpo_LsJAL7CmJkempiVwmprP6yd/exec"
    
    params = {
        "action": "Read"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            for record in data:
                esquerda = record.get('esquerda')
                direita = record.get('direita')
                frente = record.get('frete')  # Corrigido para 'frete'
                re = record.get('re')
                print(f"Esquerda: {esquerda}, Direita: {direita}, Frente: {frente}, Ré: {re}")
        except ValueError:
            print("Erro ao decodificar a resposta JSON")
    else:
        print("Erro:", response.status_code, response.text)

if __name__ == "__main__":
    read_records()
