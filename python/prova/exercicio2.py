nome = input("Digite seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

if ( media >= 6):
    print("O aluno {} foi aprovado com a media de {}.".format(nome, media))
else:
    print("O aluno {} foi reprovado com média de {}.".format(nome, media))    