Algoritmo "curso Gustavo"
Var
n1, n2, n3, n4:inteiro
media, mult, divisao:real
Inicio
escreva("Digite um numero: ")
leia(n1)
escreva("Digite outro numero: ")
leia(n2)
media <- (n1+n2)/2
escreval("A média de",n1, " e", n2, " e igual á ", media)
escreva("Digite um numero para a multiplicação do resultado da media: ")
leia(n3)
mult <- media*n3
escreval("O resultado da Multiplicação final é: ",mult)
escreva("Digite outro numero para divisão: ")
leia(n4)
divisao <- mult/n4
escreval("O resultado da divisão final é: ",divisao)
Fimalgoritmo