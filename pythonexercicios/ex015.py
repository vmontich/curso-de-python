distancia = int(input('Quilometragem percorrida: '))
dias = int(input('Dias de aluguel: '))
aluguel = 60 * dias + 0.15 * distancia
print('O valor do aluguel é de R$ {:.2f}'.format(aluguel))
