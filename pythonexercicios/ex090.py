aluno = dict()
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Média do aluno: "))
if aluno["media"] < 7:
    aluno["situacao"] = "Reprovado"
else:
    aluno["situacao"] = "Aprovado"
print(f"Nome: {aluno['nome']}; Média: {aluno['media']}; Situação: {aluno['situacao']}")
