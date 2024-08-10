turma = [[5.0, 4.5, 7.0, 5.2, 6.1], [2.1, 6.5, 8.0, 7.0, 6.7],[8.6, 7.0, 9.1, 8.7, 9.3]]
media = 0
for i in range (3):
    for j in range(5):
        media = media + turma [i] [j]
media = media / 15
print ("A media é {}".format(media))