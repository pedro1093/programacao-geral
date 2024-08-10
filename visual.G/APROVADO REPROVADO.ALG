Algoritmo "aprovado reprovado"
//veja as notas do aluno e faça uma media para sabermos se o aluno foi aprovado ou reprovado
Var
   n1, n2, media:real
Inicio
   escreva("Primeira nota: ")
   leia(n1)
   escreva("Segunda nota: ")
   leia(n2)
   media <- (n1 + n2) / 2
   se (media >= 7) entao
      escreval("O aluno foi aprovado!")
   senao
      escreval("O aluno foi reprovado")
   fimse
Fimalgoritmo