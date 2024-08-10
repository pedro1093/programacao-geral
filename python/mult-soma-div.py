#Crie um programa em Python que solicite ao usuário a entrada de dois números e uma opção. O programa deve oferecer duas opções:
# 1-Somar os números.
# 2-Multiplicar os números.
# 3-Dividir os Numeros.
#Com base na opção escolhida pelo usuário, o programa deve realizar a operação correspondente e exibir o resultado. Certifique-se de que o programa lide com entradas inválidas, como caracteres não numéricos e opções não válidas.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
op = int(input("Escolha 1 para somar, 2 para multiplicar, 3 para dividir: "))
soma = n1 + n2
mult = n1 * n2 
div = n1 / n2
if ( op == 1 ):
    print("A soma de {} com {} resulta em {}.".format(n1 , n2, soma))
elif ( op == 2): 
    print("A multiplicação de {} com {} resulta em {}.".format(n1, n2, mult))
elif ( op == 3):
    print("A divisão de {} com {} resulta em {}.".format(n1, n2, div))
else: 
    print("Nenhuma opção foi escolhida.")            