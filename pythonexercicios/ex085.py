lista = list()
pares = list()
impares = list()
lista.append(pares[:])
lista.append(impares[:])

for num in range(0, 7):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"Valores pares digitados: {lista[0]}")
print(f"Valores ímpares digitados: {lista[1]}")
