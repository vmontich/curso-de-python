# Tuplas são imutáveis
# Listas são mutáveis

print(' ')

lanche = ['hamburger', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'sorvete'
print(lanche)
lanche.append('coockie')
print(lanche)
lanche.insert(0, 'cachorro-quente')
print(lanche)
del lanche[3]
print(lanche)
lanche.pop(3)
print(lanche)
lanche.remove('suco')
print(lanche)
lanche.pop()
print(lanche)
if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)

print(' ')

valores = list(range(4,11))
print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))

print(' ')

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

print(' ')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
