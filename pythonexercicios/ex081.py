lista = []
opcao = "S"
count = 0
existe5 = False

while opcao.upper() == "S":
    num = int(input("Digite um número: "))
    lista.append(num)
    count += 1
    opcao = input("Deseja continuar? ")

print("=-" * 20)
print(lista)
print("=-" * 20)

print(f"Quantidade de números digitados: {count}")
lista.sort(reverse=True)
print(f"Lista inversamente ordenada: {lista}")
if 5 in lista:
    print("O número 5 foi digitado e está na lista")
else:
    print("O número 5 não foi digitado.")