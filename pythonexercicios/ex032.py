ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    if ano % 100 != 0:
        print("Ano bissexto")
    else:
        if ano % 400 == 0:
            print("Ano bissexto")
        else:
            print("Ano não bissexto")
else:
    print("Ano não bissexto")