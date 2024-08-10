#Tudo que está em verde são as explicações basicas de cada linha.
#Itera = "percorrer" ou "repertir"

import requests # Importa a biblioteca requests para fazer requisições HTTPS
import time # Importa a biblioteca time para manipulação do tempo

def read_records(): # Função para ler registros de uma URL especificada
    url = "https://script.google.com/macros/s/AKfycbwWPTMvM6E-TH9ng42BQ2JIqKmceiZAFT_ESmZ3W9oziZsSNWtaiQ_Z5QWgsAj3vh4-/exec"
    
    params = {
        "action": "Read"  # Parâmetro para a requisição HTTP GET
    }
    
    # Faz a requisição GET para a URL especificada com os parâmetros fornecidos
    response = requests.get(url, params=params)
    
    if response.status_code == 200: # Verifica se a resposta foi bem-sucedida
        try:
            data = response.json() # Tenta decodificar a resposta JSON
            
            
            # Itera sobre os registros recebidos
            for record in data:
                print(record['re'])  # Acessa e imprime o campo 're' do registro
                print(record['direita'])  # Acessa e imprime o campo 'direita' 
                print(record['esquerda'])
                print("--------")
                          
                
        except ValueError:
            print("Erro ao decodificar a resposta JSON") # Caso ocorra um erro na decodificação do JSON
    else:
        print("Erro:", response.status_code, response.text) # Exibe o erro se a requisição não for bem-sucedida


# Bloco principal que será executado quando o script for rodado
if __name__ == "__main__":
    while True:
        read_records() # Chama a função para ler os registros

