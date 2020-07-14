from datetime import datetime

now = datetime.now()
anoAtual = now.year
countMaiores = 0
countMenores = 0

for i in range(1, 8):
    ano = int(input("Digite o seu ano de nascimento: "))
    if anoAtual - ano >= 21:
        countMaiores = countMaiores + 1
    else:
        countMenores = countMenores + 1
print("{} pessoas atingiram a maioridade e {} ainda não atingiram".format(countMaiores, countMenores))
