#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input("Valor do produto: "))
desconto = preço - (preço * 5 / 100)
print("O valor do produto com desconto será de {}".format(desconto))
