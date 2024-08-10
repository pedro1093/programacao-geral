Algoritmo "semnome"

Var
totaldeapartamentos,totaldemoradores,valorcondominio:real
media,totalarrecadado:real
Inicio
escreval("total de apartamentos")
leia(totaldeapartamentos)
escreval("total de moradores")
leia(totaldemoradores)
escreval("valor do condominio")
leia(valorcondominio)
media <- (totaldeapartamentos / totaldemoradores)
totalarrecadado <- (totaldeapartamentos*valorcondominio)
escreval("*********************** * EDIFíCIO BOA VISTA *")
escreval("***********************************************")
escreval("* * TOTAL DE APARTAMENTOS : ",totaldeapartamentos)
escreval("* * TOTAL DE MORADORES : ",totaldemoradores)
escreval("* * VALOR DO CONDOMINIO : ",valorcondominio )
escreval("********************************************************************************")
escreval("* BALANCO FINAL *")
escreval(" MEDIA DE MORADORES/APTO :",media )
escreval(" TOTAL ARRECADADO : ",totalarrecadado)
escreval("********************************************************************************")
Fimalgoritmo