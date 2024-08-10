#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import radians, sin, tan, cos
an = float(input("Digite o valor do angulo: "))
cos = cos(radians(an))
sen = sin(radians(an))
tg = tan(radians(an))
print("O valor de seno e {:.2f}, do cosseno e {:.2f} e tangente sera {:.2f}".format(sen, cos, tg))
