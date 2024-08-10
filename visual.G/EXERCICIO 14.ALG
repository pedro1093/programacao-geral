Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/09/2023
Var
// Seção de Declarações das variáveis 
numero,op,resul:real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("digite a quantidade de pessoas:")
leia(numero)
escolha(numero)
               caso 1,2
                    resul<-numero*5
                    escreval("você gasta",resul," reais em sua viagem de moto!")
               caso 3,4,5
                    resul<-numero*10
                    escreval("você gasta",resul," reais em sua viagem de carro!")
               caso 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50
                    resul<-numero*2.5
                    escreval("você gasta",resul," reais em sua viagem de ônibus!")
               outrocaso
                        resul<-numero*1.5
                        escreval("você gasta",resul," reais em sua viagem!")
fimescolha
                    
Fimalgoritmo