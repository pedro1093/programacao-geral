Algoritmo "exercicio"

Var
valor,op,resul:real
Inicio
escreva("Digite o preço ")
leia(valor)
escreva("digite 1 para pagar a vista com 10% de desconto 2 para parcelamento em 5x sem juros, 3 para parcelamento em 10x com juros 20% ")
leia(op)
escolha op
   caso 1
         resul <- (valor*0,9)
         escreval("valor a vista 10%", resul)
   caso 2
         resul <- valor
         escreval("valor com 5x sem juros", resul)
   caso 3
         resul <- (valor * 1,2)
         escreval("valor 10x com juros 20%", resul)
   outrocaso
         escreval("numero invalido")
   fimescolha
Fimalgoritmo