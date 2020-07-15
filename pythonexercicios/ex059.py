num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
opcao = -1
while opcao != 5:
    opcao = int(input("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    
    Escolha uma opção: """))

    if opcao == 1:
        print("A soma dos dois números é {}".format(num1 + num2))
    elif opcao == 2:
        print("A multiplicação dos dois números é {}".format(num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print ("{} é maior do que {}".format(num1, num2))
        elif num2 > num1:
            print("{} é maior do que {}".format(num2, num1))
        else:
            print("{} é igual a {}".format(num1, num2))
    elif opcao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

print("Fim do programa")
