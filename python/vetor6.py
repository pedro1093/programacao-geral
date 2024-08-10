nome_vetor = []
suspeito = []
cumplice = []
assassino = []
inocente = []
n = 0
op = input("Digite algo para começar o interrogatorio: ")
while op != "s":
    nome = input("Qual o nome do suspeito: ")
    local = input("Esteve no local do crime? ")
    telefone = input("Telefonou para a vítima? ")
    perto = input("Mora perto da vítima? ")
    devia = input("Devia para a vítima? ")
    trabalho = input("Já trabalhou com a vítima? ")
    nome_vetor.append(nome)

    op = input("Digite s para sair: ")
    if local == "s":
        n+=1
    elif telefone == "s":
        n+=1
    elif perto == "s":
        n+=1
    elif devia == "s":
        n+=1
    elif trabalho == "s":
        n+=1
    
    if n == 2:
        suspeito.append(nome)
    elif n == 3 and n == 4:
        cumplice.append(nome)
    elif n == 5:
        assassino.append(nome)
    else:
        inocente.append(nome)

print("Os Assassinos")
for i in range(len(assassino)):
    print(assassino[i])

print("Os cumplices")
for i in range(len(cumplice)):
    print(cumplice[i])
    
print("suspeitos")
for i in range(len(suspeito)):
    print(suspeito[i])