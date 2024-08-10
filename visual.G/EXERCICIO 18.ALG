Algoritmo "semnome"
// Ler três notas de um aluno e calcular a média usando (se)
// Informar se ele foi aprovado ou reprovado
//reprovado (Média <= 7)  aprovado (Média >= 7)
//utilizar parabens se a media for (Média = 10)
Var
media,nota1,nota2,nota3:real
Inicio
escreval("Entre com nota 1")
leia(nota1)
escreval("Entre com nota 2")
leia(nota2)
escreval("Entre com nota 3")
leia(nota3)
media<-(nota1+nota2+nota3) / 3
se(media = 10)entao
escreval("Parabéns o aluno passou com media maxima!")
senao
     se (media >= 7)entao
        escreval("O aluno esta aprovado")
     senao
          se (media < 7)entao
             escreval("O aluno esta reprovado")
          fimse
     fimse
fimse
Fimalgoritmo
