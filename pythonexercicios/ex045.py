import random

jogadaPC = random.randrange(1, 4)
jogadaUsuario = int(input("Escolha sua jogada: (1- PEDRA / 2- PAPEL / 3- TESOURA) "))

if jogadaPC == 1:
    if jogadaUsuario == 1:
        print("Pedra vs Pedra: EMPATE")
    elif jogadaUsuario == 2:
        print("Pedra vs Papel: VOCÊ VENCEU!")
    elif jogadaUsuario == 3:
        print("Pedra vs Tesoura: VOCÊ PERDEU ")
elif jogadaPC == 2:
    if jogadaUsuario == 1:
        print("Papel vs Pedra: VOCÊ PERDEU")
    elif jogadaUsuario == 2:
        print("Papel vs Papel: EMPATE")
    elif jogadaUsuario == 3:
        print("Papel vs Tesoura: VOCÊ VENCEU")
elif jogadaPC == 3:
    if jogadaUsuario == 1:
        print("Tesoura vs Pedra: VOCÊ VENCEU")
    elif jogadaUsuario == 2:
        print("Tesoura vs Papel: VOCÊ PERDEU")
    elif jogadaUsuario == 3:
        print("Tesoura vs Tesoura: EMPATE")
