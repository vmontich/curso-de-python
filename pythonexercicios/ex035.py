import math
r1 = int(input("Primeira reta: "))
r2 = int(input("Segunda reta: "))
r3 = int(input("Terceira reta: "))

if abs(r2 - r3) < r1 and r1 < (r2 + r3):
    if abs(r1 - r3) < r2 and r2 < (r1 + r3):
        if abs(r1 - r2) < r3 and r3 < (r1 + r2):
            print("As 3 retas podem formar um triângulo")
        else:
            print("As 3 retas não podem formar um triângulo")
    else:
        print("As 3 retas não podem formar um triângulo")
else:
    print("As 3 retas não podem formar um triângulo")