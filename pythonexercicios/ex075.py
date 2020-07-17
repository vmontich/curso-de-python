num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))
num4 = int(input("Quarto número: "))
tupla = (num1, num2, num3, num4)
tuplaPar = ()

print(tuplaPar)

digitou3 = 0

for num in tupla:
    if num == 3:
        digitou3 = 1

print(f"O número 9 apareceu {tupla.count(9)} vezes")

if digitou3 == 1:
    print(f"O primeiro valor 3 foi digitado na posição {tupla.index(3) + 1}")
else:
    print("O número 3 não foi digitado")

print(f"Os números pares digitados foram ", end="")
for pos, num in enumerate(tupla):
    if num % 2 == 0:
        print(f"{num} ", end="")
