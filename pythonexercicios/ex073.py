times = ("Athlético PR", "Atlético GO", "Atlético MG", "Bahia", "Botafogo", "RB Bragantino", "Ceará", "Corinthians", "Coritiba", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Grêmio", "Internacional", "Palmeiras", "Santos", "São Paulo", "Sport", "Vasco")
print(f"Os 20 times do Brasileirão 2020 são: {times}")
print(f"Os 5 primeiros são: {times[:5]}")
print(f"Os 4 últimos são: {times[-4:]}")
print(f"Os times orgaizados em ordem alfabética são {sorted(times)}")
print(f"O Palmeiras está na posição {times.index('Palmeiras') + 1}")
