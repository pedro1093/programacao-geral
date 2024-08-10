#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
a1 = str(input("Digite o nome do aluno: "))
a2 = str(input("Digite o nome do aluno: "))
a3= str(input("Digite o nome do aluno: "))
a4 = str(input("Digite o nome do aluno: "))
lista = [a1, a2, a3, a4]
escolha = random.choice(lista)
print("O aluno escolhido para apagar o quadro foi {}".format(escolha))