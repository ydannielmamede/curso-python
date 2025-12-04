nome = input("Digitar o nome: ")
estadoCivil = input("Digitar estado civil: ")
escolaridade = input("Digitar escolaridade: ")
idade = int(input("Digitar a idade: "))
endereco = input("Digitar a endereço: ")
salario1 = float(input("Digitar primeiro salário: "))
salario2 = float(input("Digitar segundo salário: "))
salario3 = float(input("Digitar terceiro salário: "))

mediaSalario = (salario1 + salario2 + salario3) / 3
diferencaSalario = salario1 - salario2

print(f"Seu nome é: {nome}")
print(f"Seu estado civil é: {estadoCivil}")
print(f"Sua idade é: {idade}")
print(f"Seu endereço é: {endereco}")
print()
print(f"Sua média salarial é: {mediaSalario:.2f}")
print(f"A diferença de salário é: {abs(diferencaSalario):.2f}")
