lista = []
menor = -1
maior = -1
for i in range(1, 6):
    n = int(input(f"Digite um número para a posição {i}: "))
    lista.append(n)
    if i == 1:
        menor = n
        maior = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n

pos_menor = []
pos_maior = []
for i in range(0, len(lista)):
    if lista[i] == menor:
        pos_menor.append(i+1)
    elif lista[i] == maior:
        pos_maior.append(i+1)

print(f"O maior número digitado foi o {maior}. Ele aparece nas seguintes posições: {pos_maior}")
print(f"O menor número digitado foi o {menor}. Ele aparece nas seguintes posições: {pos_menor}")
