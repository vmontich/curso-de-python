num = int(input("Digite o primeiro termo para uma P.A.: "))
razao = int(input("Digite a razão da P.A.: "))
print(num)
for i in range(1, 10):
    num = num + razao
    print(num)
