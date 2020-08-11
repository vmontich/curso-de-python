def maior(*numeros):
    maior = -9999999999
    for num in numeros:
        if num > maior:
            maior = num
    print('=~' * 50)
    print(f'O maior número é {maior}')
    print('=~' * 50)


maior(1, 2, 3, 4, 5)
maior(7, 0, 11, -3)
maior(-100, -23, -12, -95)
