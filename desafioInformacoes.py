nome = input("digitar nome: ")
while len(nome) <= 3:
    nome = input("Digitar nome com mais de 4 caracteres: ")

idade = int(input("digitar idade: "))
while idade < 0 or idade > 150:
    idade = int(input("idade incorreta, digitar novamente: "))

salario = float(input("digitar salário: "))
while salario < 0:
    salario = int(input("Salário não pode ser negativo, digitar novamente: "))

sexo = input("digitar gênero: ")
while sexo != "f" and sexo != "m":
    sexo = input("Sexo incorreto, digitar novamente 'f' ou 'm': ")

estadoCivil = input("digitar estado civil: ")
while (
    estadoCivil != "s"
    and estadoCivil != "c"
    and estadoCivil != "v"
    and estadoCivil != "d"
):
    estadoCivil = input(
        "Estado civil incorreto, digitar novamente 's', 'c', 'v' ou 'd': "
    )
print("Cadastro concluído com sucesso!")
