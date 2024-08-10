import requests

def add_record():
    url = "https://script.google.com/macros/s/AKfycbw6kmCN_N102CkrnK-sg_lOOsWDgcTFjzeox0s4hkpo_LsJAL7CmJkempiVwmprP6yd/exec"
    
    params = {
        "action": "Create",
        "nome": "respiberry",
        "direita": 1,
        "esquerda": 1,
        "frente": 1,
        "re": 1
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    add_record()
