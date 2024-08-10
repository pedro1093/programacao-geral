nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if ( idade <= 18 or idade >= 65):
    print("{} você não pode ter acesso ao desconto.".format(nome))
else:
    print("{} você tem direito a desconto no ingresso.".format(nome))    