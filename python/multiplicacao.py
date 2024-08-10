#Crie um programa em Python que solicite ao usuário a entrada de dois números e uma opção. O programa deve oferecer duas opções:
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
op = int(input("Escolha 1 para multiplicação ou 2 para soma: "))
mult = n1 * n2 
soma = n1 + n2
if ( op == 1 ):
    print("A multiplicação de {} e {} resulta em {}".format(n1, n2, mult))
elif (op == 2):
    print("A soma de {} e {} resulta em {}".format(n1, n2, soma))
else:
    print("Nenhuma opção foi selecionada")    