numOriginal = int(input("Digite um número: "))
num = numOriginal
fatorial = num
while num > 1:
    fatorial = fatorial * (num - 1)
    num = num - 1
print("A fatorial de {} é igual a {}".format(numOriginal, fatorial))
