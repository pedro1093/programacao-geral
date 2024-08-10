#Você deve criar um algoritmo em Python que permita determinar se uma pessoa tem direito a um desconto no ingresso com base em sua idade. O programa deve realizar as seguintes ações:
# 1-Solicitar que o usuário digite sua idade e seu nome .
# 2-Verificar se a idade fornecida é menor que 18 anos OU maior ou igual a  65 anos.
# 3-Se a idade estiver dentro dessas faixas, exibir a mensagem "Você pode ter desconto no ingresso."
# 4-Caso contrário, mostrar a mensagem "Você não tem direito a desconto no ingresso."
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if ( idade < 18 or idade >= 65):
    print("{} você pode ter acesso ao desconto.".format(nome))
else:
    print("{} você não tem direito a desconto no ingresso.".format(nome))    