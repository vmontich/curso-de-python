n = int(input("Quantos termos deseja mostrar: "))
i = 1
fib1 = 0
fib2 = 1
aux = -1
while i <= n:
    if i == 1:
        print(fib1)
    elif i == 2:
        print(fib2)
    else:
        print(fib1 + fib2)
        aux = fib1
        fib1 = fib2
        fib2 = aux + fib1
    i += 1
