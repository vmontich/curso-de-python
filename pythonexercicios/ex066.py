count = 0
soma = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num == 999:
        break
    else:
        count += 1
        soma += num
print(f"Foram digitados {count} números")
print(f"A soma dos números digitados é {soma}")