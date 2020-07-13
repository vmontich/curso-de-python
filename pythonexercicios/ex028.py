import random
numeroPensado = random.randrange(0, 6)
numeroUsuario = int(input("Tente descobrir qual número o computador pensou: "))
if(numeroPensado == numeroUsuario):
    print("PARABÉNS! Você acertou o número.")
else:
    print("QUE PENA! Você errou o número")