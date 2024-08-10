Algoritmo "exercicio"

Var
nome:caractere
idade:inteiro
categoria:caractere
Inicio
escreval("nome do Aluno Atleta=")
leia(nome)
escreval("idade do Aluno Atleta=")
leia(idade)
se(idade>=5)e(idade<=10)entao
                           categora<-"infantil"
                           escreval("O Aluno " , nome , " esta na categoria infantil")
senao
     se(idade>=11)e(idade<=15)entao
                                   categoria<-"juvenil"
                                    escreval("O Aluno " , nome , " esta na categoria juvenil")
     senao
          se(idade>=16)e(idade<=20)entao
                                       categoria<-"junior"
                                        escreval("O Aluno " , nome , " esta na categoria junior")
     senao
          se(idade>=21)e(idade<=25)entao
                                       categoria<-"profissional"
                                        escreval("O Aluno " , nome , " esta na categoria profissional")
     senao
          se(idade>=26)entao
                       escreval("O Aluno " , nome , " não esta cadastrado em uma categoria")
                           fimse
                 fimse
           fimse
 fimse
fimalgoritmo
