Algoritmo "semnome"

Var
nome: caractere
nota: real
i,frequencia: inteiro
Inicio
para i de 1 ate 5 passo 1 faca
    escreval("Digite nome do aluno")
    leia(nome)
    escreval("Digite a nota final do aluno " + nome)
    leia(nota)
    escreval("Digite a frequencia do aluno " + nome)
    leia(frequencia)
    se (nota>=6)e(frequencia>=75)entao
      escreval("O aluno " + nome + " esta aprovado!")
    senao
      escreval("O aluno " + nome + " esta reprovado!")
    fimse
fimpara
Fimalgoritmo