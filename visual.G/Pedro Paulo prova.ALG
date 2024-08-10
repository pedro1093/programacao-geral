Algoritmo "verifique o numero lido e negativo,positivo ou é o zero"
Var
nota1,nota2,op,resultado:real

Inicio
ESCREVAL("DIGITE nota 1")
 leia (nota1)
 ESCREVAL("digite nota 2")
 leia(nota2)

 escreval("digite op 0 pra soma e 1 pra mult e 2 pra divisao e 3 pra potencia ")
 leia(op)
 se(op=0)entao
    resultado<-(nota1+nota2)
    escreval("resultado",resultado)
 senao
   se(op=1)entao
       resultado<-(nota1*nota2)
       escreval("resultado",resultado)
   senao
       se(op=2)entao
          resultado<-(nota1/nota2)
          escreval("resultado",resultado)
    senao
        se(op=3)entao
       resultado<-(nota1^nota2)
       escreval("resultado",resultado)
      senao
            escreval("op invalido")

      fimse
     fimse
   fimse
 fimse
Fimalgoritmo
