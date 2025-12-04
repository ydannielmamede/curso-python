nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "aprovado!"
elif media >= 5 and media <= 6.9:
    situacao = "recuperação!"
else:
    situacao = "reprovado!"

print(f"Média final : {media}")
print(f"Situação do aluno : {situacao}")
