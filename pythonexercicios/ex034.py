salario = float(input("Digite seu salário: "))

if salario > 1250:
    salario = salario * 1.10
else:
    salario = salario * 1.15

print("Salário com reajuste: R${:.2f}".format(salario))
