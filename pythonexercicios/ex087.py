matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_dos_pares = 0
soma_da_coluna_3 = 0
maior_valor_da_segunda_linha = -1

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f"Digite um número para a posição [{i},{j}]: "))
        matriz[i][j] = num
        if num % 2 == 0:
            soma_dos_pares += num
        if j == 2:
            soma_da_coluna_3 += num
        if i == 1:
            if num > maior_valor_da_segunda_linha:
                maior_valor_da_segunda_linha = num
for linha in matriz:
    print(f"| {linha[0]} | {linha[1]} | {linha[2]} |")

print(f"Soma dos valores pares: {soma_dos_pares}")
print(f"Soma dos elementos da coluna 3: {soma_da_coluna_3}")
print(f"Maior valor da linha 2: {maior_valor_da_segunda_linha}")

