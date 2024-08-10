#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario, com 15% de aumento.
salario = int(input("Valor do seu salario: "))
aumento =  (salario * 15 / 100)
print("O funcionario tera um aumento de {:.2f}".format(aumento))