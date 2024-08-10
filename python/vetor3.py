n = 1
media = 0
media_vetor = []
nome_vetor = []

while n <= 3:
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite um nota 1: "))
    n2 = float(input("Digite um nota 2: "))
    n3 = float(input("Digite um nota 3: "))
    n4 = float(input("Digite um nota 4: "))
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 6:
        media_vetor.append(media)
        nome_vetor.append(nome)
    else:
        print("A media do {}, e {}".format(nome, media))
        n+=1 
print("Alunos com media >= 6")
for i in range(len(media_vetor)):
    print(media_vetor[i])
    print(nome_vetor[i]) 
    