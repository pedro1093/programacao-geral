Algoritmo "Está apto a dirigir?"
//  Cria um algoritmo para descobrir a idade
//  Se idade for maior que 18 esta apto a dirigir caso contrario não
Var
   a, an, idade: inteiro
Inicio
   escreva("Ano de nascimento: ")
   leia(a)
   escreva("Ano atual: ")
   leia(an)
   idade <- (an - a)
   se (idade >= 18) entao
      escreval("Você esta apto a dirigir")
   senao
      escreval("Você não pode dirigir um carro!")
   fimse
Fimalgoritmo