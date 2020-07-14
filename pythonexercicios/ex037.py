num = int(input("Digite um número inteiro: "))
base = int(input("Em qual base deseja converter: (1- Binário / 2- Octal / 3- Hexadecimal) "))

if base == 1:
    print("{0:b}".format(num))
elif base == 2:
    print("{0:o}".format(num))
else:
    print("{0:x}".format(num))
