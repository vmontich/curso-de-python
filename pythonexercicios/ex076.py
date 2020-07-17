produtos = ('Lápis', 3.99, 'Caderno', 10.50, 'Régua', 5.20, 'Borracha', 1.99, 'Apontador', 3.25, 'Marca Texto', 8.90,
            'Mochila', 299.99, 'Livro', 89.90)

print('=' * 40)
print(f"{'PREÇOS':^40}")
print('=' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>6.2f}')
print('-' * 40)