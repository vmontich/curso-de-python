num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = 0
menor = 0

if num1 > num2:
    if num1 > num3:
        maior = num1
    else:
        maior = num3
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3
print("Maior: {}".format(maior))

if num1 < num2:
    if num1 < num3:
        menor = num1
    else:
        menor = num3
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3
print("Menor: {}".format(menor))
