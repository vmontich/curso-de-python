from random import randint

def sorteia():
    lst = []
    for i in range(0, 5):
        lst.append(randint(1, 10))
    print(f'Lista criada: {lst}')
    return lst

def soma_par(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos números pares da lista é igual a {soma}')


lista = sorteia()
soma_par(lista)
