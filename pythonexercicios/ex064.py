countNum = 0
somaNum = 0
num = -1
while num != 999:
    num = int(input("Digite um número inteiro: [999 para sair] "))
    if num != 999:
        countNum += 1
        somaNum += num
print("Fora digitados {} números".format(countNum))
print("A soma dos números digitados é {}".format(somaNum))
