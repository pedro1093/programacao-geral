Algoritmo "semnome"

Var
numero,resul:real


Inicio
escreval("Digite o numero de rosas para seu buque:")
leia(numero)
escolha(numero)
      caso 1,2,3,4,5,6,7,8,9,10,11
           resul<-(numero*5)
           escreval("O valor do buque pequeno será: ",resul, "reais")
      outrocaso
           resul<-(numero*3)
           escreval("O valor do buque grande será: ",resul, "reais")
fimescolha
Fimalgoritmo