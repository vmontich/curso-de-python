pessoa = dict()
pessoas = list()
mulheres = list
pessoas_mais_velhas = list()
decisao = "S"
soma_das_idades = 0
media = 0

while decisao.upper() != "N":
    pessoa["nome"] = input("Nome: ")
    pessoa["idade"] = int(input("Idade: "))
    soma_das_idades += pessoa["idade"]
    pessoa["sexo"] = input("Sexo [F/M]: ")
    pessoas.append(pessoa.copy())
    pessoa.clear()
    decisao = input("Deseja continuar? [S/N] ")

media = soma_das_idades / len(pessoas)
print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"A média de idade dessas pessoas é de {media:.1f} anos")
print(f"Lista das mulheres cadastradas: ", end="")
for p in pessoas:
    if p["sexo"].upper() == "F":
        print(f"{p['nome']} ", end="")

print("")

print(f"Lista das pessoas com idade acima da média: ", end="")
for p in pessoas:
    if p["idade"] > media:
        print(f"{p['nome']} ", end="")
