nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if ( idade >=5 and idade <=10):
    print("{} você esta na categoria infantil.".format(nome))
elif ( idade >=11 and idade <=15):
    print("{} você esta na categoria Juvenil.".format(nome)) 
elif ( idade >=16 and idade <=20):
    print("{} você esta na categoria Junior.".format(nome))
elif ( idade >=21 and idade <=25):
    print("{} você esta na categoria Profissional.".format(nome))
else:
    print("{} sua categoria não esta cadastrada.".format(nome))           