extenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        break;
    else:
        print("Tente novamente! ", end="")
print(f"Você digitou o número {extenso[num - 1]}")
