while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    else:
        print("#"*25)
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
        print("#" * 25)
