#Escreva um programa que leia o valor em metros e o exiba em centimetros a milimetros.
n1 = float(input("Digite uma medida em metros: "))
c = n1 * 100
m = n1 * 1000
print("Isso resulta em {:.0f}cm, e em {:.0f}mm.".format(c, m))