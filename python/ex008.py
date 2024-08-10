#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere $1,00 = $5,02. 
n1 = float(input("Quantos reais você tem consigo? R$"))
print("De acordo com seu saldo de R${}, a conversão para o Dolar ficara cotada em US${:.2f} !".format(n1, (n1/5.02)))