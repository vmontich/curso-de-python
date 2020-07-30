from datetime import date

dados_pessoais = dict()

dados_pessoais["nome"] = input("Nome: ")
dados_pessoais["ano_nascimento"] = int(input("Ano de Nascimento: "))
dados_pessoais["ctps"] = input("Carteira de Trabalho: ")

ano_atual = date.today().year
dados_pessoais["idade"] = ano_atual - dados_pessoais["ano_nascimento"]

if dados_pessoais["ctps"] != 0:
    dados_pessoais["ano_contratacao"] = input("Ano de contratação: ")
    dados_pessoais["salario"] = input("Salário: ")
    dados_pessoais["idade_aposentadoria"] = dados_pessoais["idade"] + 30

print("-=" * 30)
print("## Dados Pessoais ##")
for k, v in dados_pessoais.items():
    print(f"{k}: {v}")
print("-=" * 30)
