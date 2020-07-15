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
