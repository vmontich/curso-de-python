velocidade = int(input("velocidade do carro: "))
if velocidade > 80:
    print("Você foi multado!")
    valor = (velocidade - 80) * 7
    print("Valor total da multa: R${:.2f}".format(valor))