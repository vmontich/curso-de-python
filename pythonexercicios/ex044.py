preco = float(input("Valor do produto: "))
forma = int(input("Forma de pagamento: (1- À vista DINHEIRO/CHEQUE | 2- À vista CARTÃO | 3- Parcelado 2x | 4- Parcelado 3x ou mais) "))

if forma == 1:
    print("Valor do produto: R${:.2f}".format(preco * 0.9))
elif forma == 2:
    print("Valor do produto: R${:.2f}".format(preco * 0.95))
elif forma == 3:
    print("Valor do produto: R${:.2f}".format(preco))
else:
    print("Valor do produto: R${:.2f}".format(preco * 1.20))