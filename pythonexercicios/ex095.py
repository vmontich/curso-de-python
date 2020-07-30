jogadores = list()
jogador = dict()
gols = list()
decisao_1 = "S"
decisao_2 = 1000
count = 1
soma_de_gols = 0

while decisao_1.upper() != "N":
    print("~~" * 40)
    soma_de_gols = 0
    jogador["cod"] = count
    jogador["nome"] = str(input("Nome do jogador: "))
    jogador["qtd_partidas"] = int(input("Quantidade de partidas jogadas no campeonato: "))
    for i in range(0, jogador["qtd_partidas"]):
        gols.append(int(input(f"Quantos gols {jogador['nome']} fez na partida {i + 1}? ")))
        soma_de_gols += gols[i]
    jogador["tot_gols"] = soma_de_gols
    jogador["gols"] = gols[:]
    jogadores.append(jogador.copy())
    count += 1
    jogador.clear()
    gols.clear()
    decisao_1 = str(input("Deseja continuar inserindo jogadores? (S/N)")).upper()

print("-=" * 40)


while True:
    print("cod - nome - partidas - gols")
    for jogador in jogadores:
        print(f"{jogador['cod']} | {jogador['nome']} | {jogador['qtd_partidas']} | {jogador['tot_gols']}")
    decisao_2 = int(input("Mostrar dados de qual jogador? "))
    if decisao_2 == 0:
        break
    else:
        print(f"\n-- DADOS DO JOGADOR {jogadores[decisao_2 - 1]['nome']} --")
        for i in range(1, len(jogadores[decisao_2 - 1]['gols'])+1):
            print(f"No {i}º jogo fez {jogadores[decisao_2 - 1]['gols'][i-1]} gol(s)")
        print()


