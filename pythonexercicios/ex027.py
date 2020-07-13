nome = input("Digite o seu nome completo: ").strip()
print("Primeiro Nome: {}".format(nome.split()[0]))
print("Último Nome: {}".format(nome.split()[len(nome.split()) - 1]))
