totalGasto = 0
maisDe1000 = 0
valorDoMaisBarato = pow(1000, 1000)
nomeDoMaisBarato = "a"

while True:
    print("*" * 120)
    produto = input("Nome do produto: ")
    valor = float(input("Valor do produto: "))
    totalGasto += valor
    if valor > 1000:
        maisDe1000 += 1
    if valor < valorDoMaisBarato:
        valorDoMaisBarato = valor
        nomeDoMaisBarato = produto
    opcao = input("Deseja continuar? [S / N] ").upper()
    if opcao == "N":
        break
print("*" * 120)
print(f"Total gasto: {totalGasto}")
print(f"Quantidade de produtos com valor acima dos R$ 1.000,00: {maisDe1000}")
print(f"Produto mais barato: {nomeDoMaisBarato}")
print("*" * 120)
