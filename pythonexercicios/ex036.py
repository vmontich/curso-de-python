valor = float(input("Valor da casa: "))
salario = float(input("Seu salário: "))
tempo = float(input("Em quantos anos pagará: "))
prestacao = valor / (tempo * 12)

if prestacao > salario * 0.3:
    print("O empréstimo não será aprovado nestas condições")
else:
    print("Empréstimo aprovado! Valor da prestação mensal: R${:.2f}".format(prestacao))
