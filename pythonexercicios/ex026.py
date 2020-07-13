frase = input("Digite uma frase: ").strip().upper()
print("Quantidade de letras A: {}".format(frase.upper().count("A")))
print("Posição da primeira ocorrência de A: {}".format(frase.find("A") + 1))
print("Posição da última ocorrência de A: {}".format(frase.rfind("A") + 1))
