from datetime import datetime

ano = int(input("Digite seu ano de nascimento: "))
now = datetime.now()
anoAtual = now.year
idade = anoAtual - ano

if idade == 18:
    print("Está na hora de você se alistar para o exército")
elif idade < 18:
    print("Ainda não chegou a hora de você se alistar para o exército. Faltam {} anos".format(18 - idade))
else:
    print("Já se passaram {} anos para você se alistar para o exército".format(idade - 18))
