num = int(input("Digite um número: "))
ehPrimo = 1
for i in range(2, num):
    if num % i == 0:
        ehPrimo = 0
if ehPrimo == 1:
    print("O número {} é primo".format(num))
else:
    print("O número {} não é primo".format(num))
