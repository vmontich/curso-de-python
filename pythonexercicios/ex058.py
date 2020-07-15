import random
numeroPensado = random.randrange(0, 11)
numeroUsuario = -1

while numeroPensado != numeroUsuario:
    numeroUsuario = int(input("Tente descobrir qual número o computador pensou: (de 0 a 10) "))
print("PARABÉNS! Você acertou o número.")