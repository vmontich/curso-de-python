matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f"Digite um número para a posição [{i},{j}]: "))
        matriz[i][j] = num
for linha in matriz:
    print(f"| {linha[0]} | {linha[1]} | {linha[2]} |")
