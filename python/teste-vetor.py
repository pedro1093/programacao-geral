nota = [60, 95, 80, 50, 98]
print(nota[3])
nota.append(20)
nota.append(75)
Lista_frutas = ["abacaxi", "pera", "uva", "abacaxi"]
Lista_frutas.append("maça")
Lista_frutas.append("laranja")
print(Lista_frutas[1])

for i in range(len(nota)):
    print(nota[i])
for i in range(len(Lista_frutas)):
    print(Lista_frutas[i])
    
del nota[6]