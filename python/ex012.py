#crie um programa que leia um numero qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um numero: 6.127, o numero 6.127 tem a parte inteira 6
from math import trunc
n1 = float(input("Digite um numero: "))
print("O valor digitado foi {} e sua porção inteira é {}".format(n1, trunc(n1)))
#usando uma importação unica da biblioteca math 

n1 = float(input("Digite um valor: "))
print("O valor digitado foi {} e sua porção inteira é {}".format(n1, int(n1)))
#usando os comnados já acessiveis do python para chegar no resultado acima