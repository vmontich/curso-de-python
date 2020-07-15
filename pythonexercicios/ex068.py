import random

countVitorias = 0

while True:
    jogadaPC = random.randrange(0, 6)
    print("=" * 30)
    parOuImpar = int(input("Par(1) ou Ímpar(2)? "))
    jogadaUsuario = int(input("Escolha seu número (de 0 a 5): "))
    print(f"Resultado: {jogadaPC + jogadaUsuario}")
    if parOuImpar == 1:
        if (jogadaPC + jogadaUsuario) % 2 != 0:
            break
        else:
            print("Você venceu!")
            countVitorias += 1
    else:
        if (jogadaPC + jogadaUsuario) % 2 == 0:
            break
        else:
            print("Você venceu!")
            countVitorias += 1
print(f"Fim de jogo! Você conseguiu vencer {countVitorias} seguidas")
print("=" * 30)