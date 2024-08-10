Algoritmo "Peso IMC"
// Faça umacalculadora que calcule o imc
Var
  m, a, imc:real
Inicio
      escreva("Qual seu peso (Kg): ")
      leia(m)
      escreva("Qual sua altura (m): ")
      leia(a)
      imc <- m / (a ^ 2)
      escreval("Seu IMC é: ", imc:5:2)
      se (imc >= 18.5) e (imc < 25) entao
         escreval("Parabéns, você está no seu peso ideal!")
      senao
         escreval("Você não esta na faixa de peso ideal!")
      fimse
      



Fimalgoritmo