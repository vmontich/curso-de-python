import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

print('{} apagará a lousa.'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))
