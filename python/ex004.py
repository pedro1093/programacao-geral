#Crie um algoritmo que leia um numero e mostre seu dobro seu triplo e sua raiz quadrada.
n1 = int(input("Digite um numero: "))
d = n1 * 2
t = n1 * 3
e = n1 ** (1/2)
print("O dobro de {} e {}, seu triplo será {}, e por fim sua raiz é {:.2f}.".format(n1, d, t, e)) 