dados_jogador = dict()
gols_jogador = list()
total_de_gols = 0
dados_jogador["nome"] = input("Nome do jogador: ")
dados_jogador["qtd_partidas"] = int(input("Quantidade de partidas jogadas no campeonato: "))
for i in range(0, dados_jogador["qtd_partidas"]):
    gols_jogador.append(int(input(f"Quantos gols {dados_jogador['nome']} fez na partida {i+1}? ")))
dados_jogador["gols"] = gols_jogador

for gol in dados_jogador["gols"]:
    total_de_gols += gol

dados_jogador["total_de_gols"] = total_de_gols
dados_jogador["media_de_gols"] = total_de_gols / dados_jogador["qtd_partidas"]

print("-=" * 30)
print(dados_jogador)
print("-=" * 30)

