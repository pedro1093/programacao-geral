Algoritmo "semnome"
Var
   x,y,resultado : real
   operacao : caractere

funcao soma(a, b:real):real
var
   res: real
Inicio
    res <- a + b
    retorne res
fimfuncao

funcao multiplica(a, b:real): real
var
   res:real
inicio
   res <- a * b
   retorne res
fimfuncao

funcao divide(a, b:real): real
var
   res:real
inicio
   se b <> 0 entao
      res <- a / b
   senao
        escreval("Erro: Divisão por zero!")
   fimse
   retorne res
fimfuncao

inicio
    escreval("Digite o primeiro número : ")
    leia(x)
    
    escreval("Digite a operação que deseja: (+, *, /):")
    leia(operacao)
    
    escreval("Digite o segundo número : ")
    leia(y)
    
    escolha operacao
       caso "+"
           resultado <- soma(x, y)
       caso "*"
           resultado <- multiplica(x, y)
       caso "/"
           resultado <- divide(x, y)
       caso contrario
            escreval("Operação invalida!")
    fimescolha

    escreval("Resultado: ", resultado)

Fimalgoritmo