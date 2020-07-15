print("$" * 24)
print("    CAIXA ELETRÔNICO    ")
print("$" * 24)

valorSaque = int(input("Quanto você deseja sacar?: R$"))

count50 = 0
count20 = 0
count10 = 0
count1 = 0

while True:
    if valorSaque - 50 >= 0:
        valorSaque = valorSaque - 50
        count50 += 1
    elif valorSaque - 20 >= 0:
        valorSaque = valorSaque - 20
        count20 += 1
    elif valorSaque - 10 >= 0:
        valorSaque = valorSaque - 10
        count10 += 1
    elif valorSaque - 1 >= 0:
        valorSaque = valorSaque - 1
        count1 += 1
    else:
        break
if count50 > 0:
    print(f"Nota(s) de 50: {count50}")
if count20 > 0:
    print(f"Nota(s) de 20: {count20}")
if count10 > 0:
    print(f"Nota(s) de 10: {count10}")
if count1 > 0:
    print(f"Nota(s) de 1: {count1}")
