import requests  # Importa a biblioteca requests para fazer requisições HTTP
import time  # Importa a biblioteca time para manipulação do tempo
import RPi.GPIO as GPIO  # Importa a biblioteca RPi.GPIO para controle dos pinos GPIO

# Configuração inicial dos GPIOs
GPIO.setmode(GPIO.BCM)  # Usa o número BCM dos pinos GPIO
GPIO.setwarnings(False)

# Dicionário para mapear ação para o número do pino GPIO
actions_pins = {
    're': 4,
    'direita': 2,
    'esquerda': 3
}

# Configurar os pinos GPIO como saída
for pin in actions_pins.values():
    GPIO.setup(pin, GPIO.OUT)

def read_records():  # Função para ler registros de uma URL especificada
    url = "https://script.google.com/macros/s/AKfycbwWPTMvM6E-TH9ng42BQ2JIqKmceiZAFT_ESmZ3W9oziZsSNWtaiQ_Z5QWgsAj3vh4-/exec"
    
    params = {
        "action": "Read"  # Parâmetro para a requisição HTTP GET
    }
    
    # Faz a requisição GET para a URL especificada com os parâmetros fornecidos
    response = requests.get(url, params=params)
    
    if response.status_code == 200:  # Verifica se a resposta foi bem-sucedida
        try:
            data = response.json()  # Tenta decodificar a resposta JSON
            
            # Itera sobre os registros recebidos
            for record in data:
                for action, pin in actions_pins.items():
                    value = record.get(action)  # Obtém o valor correspondente à ação
                    if value is not None:
                        # Define o estado do pino GPIO com base no valor recebido
                        GPIO.output(pin, GPIO.HIGH if value else GPIO.LOW)
                
        except ValueError:
            print("Erro ao decodificar a resposta JSON")  # Caso ocorra um erro na decodificação do JSON
    else:
        print("Erro:", response.status_code, response.text)  # Exibe o erro se a requisição não for bem-sucedida

def clear_pins():  # Função para limpar (desligar) os pinos GPIO
    for pin in actions_pins.values():
        GPIO.output(pin, GPIO.LOW)  # Define o pino GPIO como baixo (desligado)

# Bloco principal que será executado quando o script for rodado
if __name__ == "__main__":
    try:
        while True:
            read_records()  # Chama a função para ler os registros
            time.sleep(3)  # Pausa a execução por 3 segundos
            # Chama a função para limpar os pinos a cada 10 segundos (por exemplo)
            if time.time() % 10 < 3:  # Pequeno ajuste para garantir que o clear_pins seja chamado pelo menos uma vez a cada 10 segundos
                clear_pins()
    except KeyboardInterrupt:
        GPIO.cleanup()  # Limpa a configuração dos GPIO ao finalizar o script
