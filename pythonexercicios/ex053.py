frase = input("Digite uma frase: ").replace(" ", "")
aux = len(frase) - 1
ehPalindromo = 1
for i in range(0, len(frase)):
    if aux >= i:
        if frase[i] != frase[aux]:
            ehPalindromo = 0
        aux = aux - 1
if ehPalindromo == 1:
    print("Esta frase é um palíndromo")
else:
    print("Esta frase não é um palíndromo")
