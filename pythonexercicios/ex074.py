from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(numeros)

print(f"Maior número da tupla: {max(numeros)}")
print(f"Menor número da tupla: {min(numeros)}")