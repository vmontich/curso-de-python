import time


def contador(inicio, fim, salto):
    print('=-' * 30)
    print(f'Contagem de {inicio} até {fim} de {salto} em {salto}')
    soma = inicio
    while soma <= fim:
        time.sleep(0.5)
        print(f'{soma} ', end='')
        soma += salto
    print('FIM!')
    print('=-' * 30)


ni = int(input('Digite o número inicial: '))
nf = int(input('Digite o número final: '))
s = int(input('Digite o salto: '))
contador(ni, nf, s)