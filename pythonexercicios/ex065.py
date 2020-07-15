countNum = 0
somaNum = 0
menorNum = pow(1000, 1000)
maiorNum = -1
escolha = "S"

while escolha != "N":
    num = int(input("Digite um número: "))
    countNum += 1
    somaNum += num
    if num < menorNum:
        menorNum = num
    if num > maiorNum:
        maiorNum = num
    escolha = input("Deseja continuar? [S / N] ").upper()
print("A média dos números digitados é {:.1f}".format(somaNum / countNum))
print("O menor número digitado foi {}".format(menorNum))
print("O maior número digitado foi {}".format(maiorNum))