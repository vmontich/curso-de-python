lista = []

for i in range(0, 5):
    num = int(input("Digite um número inteiro: "))
    if i == 0:
        lista.append(num)
    else:
        for j in range(0, len(lista)):
            if num <= lista[j]:
                lista.insert(j, num)
                break
            elif j == len(lista) - 1:
                lista.append(num)

print(lista)
