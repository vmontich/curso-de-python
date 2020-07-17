palavras = ('programar', 'phyton', 'logica', 'desenvolvimento',
            'string', 'curso', 'video', 'codificar',
            'algoritmo', 'linguagem', 'programacao', 'pratica',
            'teoria', 'javascript', 'automatizar', 'aprendizado')

for p in palavras:
    print(f"\nNa palavra {p.upper()}, temos: ", end="")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f"{letra} ", end="")