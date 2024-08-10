n = 1
idade_vetor = []
altura_vetor = []

while n <= 5:
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    idade_vetor.append(idade)
    altura_vetor.append(altura)
    n += 1
idade_vetor.reverse()
altura_vetor.reverse()
for i in range(len(idade_vetor)):
    print(idade_vetor[i])
for i in range(len(altura_vetor)):
    print(altura_vetor[i])
