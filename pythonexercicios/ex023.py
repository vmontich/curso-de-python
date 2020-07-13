import math
numStr = input("Digite um número entre 0 e 9999: ")
numInt = int(numStr)

div1 = math.floor(numInt / 1000)
resto1 = numInt % 1000
div2 = math.floor(resto1 / 100)
resto2 = resto1 % 100
div3 = math.floor(resto2 / 10)
resto3 = resto2 % 10

print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(resto3, div3, div2, div1))

