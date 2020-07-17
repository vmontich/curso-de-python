lista = []

decisao = "S"
while decisao.upper() == "S":
    num = int(input("Digite um valor inteiro para adicionar à lista: "))
    if num in lista:
        print(f"O valor {num} já está na lista.")
    else:
        lista.append(num)
    decisao = input("Deseja continuar? ")
lista.sort()
print(f"Lista final: {lista}")
