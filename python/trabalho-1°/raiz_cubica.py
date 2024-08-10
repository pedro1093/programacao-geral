n1 = int(input("Entre com raiz de um numero: "))
raiz = (n1**(1/3))
print("{:.2f}".format(raiz))
if n1 >= 10:
    print("É necessario uso de calculadora") 
else: 
    print("Não e necessario o uso de calculadoras")        