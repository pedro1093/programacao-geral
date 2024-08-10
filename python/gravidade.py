#Faça um programa que leia seu peso na terra e escolha o numero de um planeta assim calculando qual sera o seu peso neste planeta.
# A formula para calcular o peso, considerando a gravidade relativa de cada um deles é: peso no planeta = peso na terra / 10 * gravidade 
print("-" * 20)
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
print("-" * 20)
op = int(input(" \n Veja as opções abaixo e selecione a que deseja.\n Digite 1 para Mércurio. \n Digite 2 para Vênus. \n Digite 3 para Marte. \n Digite 4 para Júpiter. \n Digite 5 para Saturno. \n Digite 6 para Urano. \n Escolha um número: "))
mer = peso / 10 * 0.37
ven = peso / 10 * 0.88
mar = peso / 10 * 0.38
jup = peso / 10 * 2.64
sat = peso / 10 * 1.15
ura = peso / 10 * 1.17
print("")
if ( op == 1):
    print (" {} seu peso convertido para Mércurio sera {:.2f}".format(nome, mer))
elif ( op == 2):
    print (" {} seu peso convertido para Vênus sera {:.2f}".format(nome, ven))
elif ( op == 3):
    print (" {} seu peso convertido para Marte sera {:.2f}".format(nome, mar))
elif ( op == 4):
    print (" {} seu peso convertido para Júpiter sera {:.2f}".format(nome, jup))
elif ( op == 5):
    print (" {} seu peso convertido para Saturno sera {:.2f}".format(nome, sat))
elif ( op == 6):
    print (" {} seu peso convertido para Urano sera {:.2f}".format(nome, ura))
else:
    print ("Nehum planeta foi selecionado")    