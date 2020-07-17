lista = []
lista_par = []
lista_impar = []
opcao = "S"

while opcao.upper() == "S":
    num = int(input("Digite um número inteiro: "))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    opcao = input("Deseja continuar? [S / N] ")

print(f"Lista principal: {lista}")
print(f"Lista de números pares: {lista_par}")
print(f"Lista de números ímpares: {lista_impar}")

