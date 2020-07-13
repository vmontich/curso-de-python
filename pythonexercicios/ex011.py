a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
area = a * l
qtdTinta = area / 2
print('Esta parede possui {}m2. Você precisará de {:.2f}l de tinta para pintá-la'.format(area, qtdTinta))
