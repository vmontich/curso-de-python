distancia = float(input("Digite a distância da viagem: "))
if distancia <= 200:
    print("Preço da passagem: R${:.2f}".format(distancia * 0.50))
else:
    print("Preço da passagem: R${:.2f}".format(distancia * 0.45))
