'''
num = int(input("Digite o primeiro termo para uma P.A.: "))
razao = int(input("Digite a razão da P.A.: "))
n = 1
while n < 11:
    if n == 1:
        print(num)
    else:
        num = num + razao
        print(num)
    n = n + 1
'''

num = int(input("Digite o primeiro termo para uma P.A.: "))
razao = int(input("Digite a razão da P.A.: "))
termos = 1

while termos != 0:
    termos = int(input("Quantos termos deseja mostrar? "))
    if termos > 0:
        print(num)
        for i in range(1, termos + 1):
            num = num + razao
            print(num)
