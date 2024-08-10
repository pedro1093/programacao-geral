#faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
alt = float(input("Qual a altura da sua parede? "))
larg = float(input("Qual a largura da sua parede? "))
area = alt * larg
print("Em uma parde com {}m de altura e {}m de largura sua aréa será de {}m²!".format(alt, larg, area))
tinta = area / 2
print("A quantidade de tinta necessaria pra pintar essa parede sera {}l de tinta.".format(tinta))