Algoritmo "semnome"

Var
opcao,nome: caractere
nota: real
frequencia: inteiro
Inicio
escreval("Digite c para começar a calcular")
leia(opcao)
enquanto (opcao="c") faca
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
escreval("Digite c para continuar a calcular ou s para sair")
leia(opcao)
fimenquanto
Fimalgoritmo