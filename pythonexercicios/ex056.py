somaDasIdades = 0
idadeHomemMaisVelho = 0
homemMaisVelho = ""
countMulheresMenoresDe20 = 0
for i in range(1, 5):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: (H / M) ")

    somaDasIdades = somaDasIdades + idade

    if idade > idadeHomemMaisVelho and sexo.upper() == "H":
        idadeHomemMaisVelho = idade
        homemMaisVelho = nome
    if sexo.upper() == "M" and idade < 20:
        countMulheresMenoresDe20 = countMulheresMenoresDe20 + 1

print("Média de idade do grupo: {:.1f}".format(somaDasIdades / 4))
print("Homem mais velho: {}".format(homemMaisVelho))
print("Quantidade de mulheres menores de 20 anos: {}".format(countMulheresMenoresDe20))
