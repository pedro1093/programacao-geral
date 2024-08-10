Algoritmo "exercicio"

Var
nota1,nota2,nota3,nota4,resul,media:real
Inicio
 escreval ( "entre com nota1")
leia (nota1)
escreval ("entre com nota2")
leia (nota2)
escreval ("entre com nota3")
leia (nota3)
escreval ("entre com nota4")
leia (nota4)
media<-(nota1+nota2+nota3+nota4) / 4
resul<-media*0.6
     se (resul >= 5)entao
        escreval("O aluno esta aprovado")
     senao
             escreval("O aluno esta reprovado")
         fimse
Fimalgoritmo