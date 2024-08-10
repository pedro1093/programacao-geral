op = "s"
while  (op != "s"):
    n1 = float(input("Digite a nota do exercicio: "))
    n2 = float(input("Digite a nota do trabalho: "))
    n3 = float(input("Digite a nota da prova: "))
    n4 = float(input("Digite a nota de participação: "))
    soma = n1 + n2 + n3 + n4
    media = soma/4
    print("Média do aluno é", media)
    