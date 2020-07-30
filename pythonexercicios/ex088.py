import random

jogos_mega_sena = list()
jogo = list()
qtd_jogos = int(input("Quantidade de jogos que deseja criar: "))
for i in range(0, qtd_jogos):
    for j in range(0, 6):
        jogo.append(random.randint(1, 60))
    jogo.sort()
    jogos_mega_sena.append(jogo[:])
    jogo.clear()

print("Os se")
for i in range(0, len(jogos_mega_sena)):
    print(jogos_mega_sena[i])
