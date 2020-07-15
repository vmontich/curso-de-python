maioresDe18 = 0
homens = 0
mulheresMenoresDe20 = 0

while True:
    print("~" * 50)
    idade = int(input("Idade: "))
    sexo = input("Sexo [M / F]: ").upper()
    if idade >= 18:
        maioresDe18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheresMenoresDe20 += 1
    opcao = input("Deseja continuar? [S / N] ").upper()
    if opcao == "N":
        break
print("~" * 50)
print(f"Maiores de 18 anos: {maioresDe18}")
print(f"Homens: {homens}")
print(f"Mulheres menores de 20 anos: {mulheresMenoresDe20}")
print("~" * 50)
