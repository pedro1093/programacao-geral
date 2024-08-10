Algoritmo "exercicio"
Var
num1,num2,op,resul:real
Inicio
escreva ("entre com num1 = ")
leia (num1)
escreva ("entre com num2 = ")
leia (num2)
   escreva("entre com 1 soma,2 subtrair, 3 multiplicar, 4 dividir")
leia (op)
   escolha op
      caso 1
         resul <- (num1+num2)
         escreval("resultado", resul)
      caso 2
          resul <- (num1-num2)
          escreval("resultado", resul)
      caso 3
           resul <- (num1*num2)
           escreval("resultado", resul)
      caso 4
           resul <- (num1/num2)
           escreval("resultado", resul)
      outrocaso
           escreval("op invalido")
           
fimescolha
Fimalgoritmo