galera = list()
decisao = "S"

while decisao.upper() == "S":
    pessoa = list()
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    pessoa.append(nome)
    pessoa.append(peso)
    galera.append(pessoa[:])
    pessoa.clear()
    decisao = input("Deseja continuar? [S / N] ")
print(f"Foram cadastradas {len(galera)} pessoas")
print("As pessoas mais pessadas (>= 100Kg) são: ")
for pessoa in galera:
    if pessoa[1] >= 100:
        print(f"{pessoa[0]}: {pessoa[1]:.2f}Kg")
print("As pessoas mais leves (<= 65Kg) são: ")
for pessoa in galera:
    if pessoa[1] <= 65:
        print(f"{pessoa[0]}: {pessoa[1]:.2f}Kg")