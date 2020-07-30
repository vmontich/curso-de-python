from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
ranking = list()
jogadas["jogador1"] = randint(1, 6)
jogadas["jogador2"] = randint(1, 6)
jogadas["jogador3"] = randint(1, 6)
jogadas["jogador4"] = randint(1, 6)

for k, v in jogadas.items():
    print(f"O jogador {k} tirou o número {v}")
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print("-=" * 30)
print("     === RANKING === ")
for i, v in enumerate(ranking):
    print(f"{i+1}º Lugar: {v[0]} com {v[1]}")
    sleep(1)
