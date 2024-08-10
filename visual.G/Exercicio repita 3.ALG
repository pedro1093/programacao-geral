Algoritmo "semnome"

Var
nomes: vetor[1..10] de caractere
notas: vetor[1..10] de real
situacoes: vetor[1..10] de caractere
i: inteiro
frequencias: vetor[1..10] de inteiro
Inicio
para i de 1 ate 10 passo 1 faca
    escreval("Digite nome do aluno")
    leia(nomes[i])
    escreval("Digite a nota final do aluno " + nomes[i])
    leia(notas[i])
    escreval("Digite a frequencia do aluno " + nomes[i])
    leia(frequencias[i])
    se (notas[i]>=6)e(frequencias[i]>=75)entao
      situacoes[i]<-"Aprovado"
    senao
      situacoes[i]<-"reprovado"
    fimse
fimpara

para i de 1 ate 10 passo 1 faca
   escreval("O aluno" + nomes[i] + " foi " + situacoes[i])
fimpara
Fimalgoritmo