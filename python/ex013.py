#faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjascente: "))
h = hypot(co, ca)
print("O valor da hipotenusa sera {:.2f}".format(h))

ca = float(input("Comprimento do cateto oposto: "))
co = float(input("Comprimento do cateto adjascente: "))
hi = (ca ** 2 + co ** 2) ** (1/2) #Função matematica para calcular a hipotenusa  ( ** 2 -> serve para elevar a raiz quadrada)
print("O valor da hipotenusa sera de {:.2f}".format(hi)) 
