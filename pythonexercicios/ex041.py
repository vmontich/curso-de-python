from datetime import datetime

now = datetime.now()
anoAtual = now.year
ano = int(input("Ano de nascimento do atleta: "))
idade = anoAtual - ano

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SENIOR")
else:
    print("MASTER")
