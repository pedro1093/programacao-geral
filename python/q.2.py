resultados_vetor = []
op = "s"
op = input("Digite algo para começar: ")
while  (op != "s"):
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite + para adição, - subtração, * multiplicação e / para divisão ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == '+':
            resultado = (num1 + num2)
        elif operacao == '-':
            resultado = (num1 - num2)
        elif operacao == '*':
            resultado = (num1 * num2)
        elif operacao == '/':
            resultado = (num1 / num2)
        else:
            print("Operação inválida. Tente novamente.")
        resultados_vetor.append(resultado)
        op = input("digite 's', para sair. ")
print("O resultado das contas serão, {}".format(resultados_vetor))