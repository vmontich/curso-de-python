import math
co = int(input('Valor do cateto oposto: '))
ca = int(input('Valor do cateto adjacente: '))
print('Valor da hipotenusa: {:.2f}'.format(math.hypot(co, ca)))
