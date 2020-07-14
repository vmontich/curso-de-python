maiorPeso = -1
menorPeso = -1
for i in range(1, 6):
    peso = float(input("Digite o peso: "))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print("Maior peso: {}. Menor peso: {}.".format(maiorPeso, menorPeso))