num_parenteses = 0
expressao = input("Digite uma expressão com aberturas e fechamentos de parênteses: ")
for char in expressao:
    if char == "(":
        num_parenteses += 1
    elif char == ")":
        num_parenteses -= 1
if num_parenteses == 0:
    print("Parabéns! Você digitou uma expressão correta.")
elif num_parenteses < 0:
    print("Cuidado! A expressão está incorreta. Existe mais fechamentos de parênteses do que aberturas.")
else:
    print("Cuidado! A expressão está incorreta. Existe mais aberturas de parênteses do que fechamentos.")