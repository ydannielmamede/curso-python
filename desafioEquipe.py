salarioColaborador = float(input("Digite o salário atual do colaborador: "))

#Salários até 280
if salarioColaborador <= 280:
    aumentopercentual = "20%"
    valorAumento = salarioColaborador*0.20
    novoSalario = (salarioColaborador+valorAumento)

#Salários entre 280 e 700
elif salarioColaborador >280 and salarioColaborador<=700:
    aumentopercentual = "15%"
    valorAumento = salarioColaborador*0.15
    novoSalario = (salarioColaborador+valorAumento)

#Salários entre 700 e 1500
elif salarioColaborador > 700 and salarioColaborador<=1500:
    aumentopercentual = "10%"
    valorAumento = salarioColaborador*0.10
    novoSalario = (salarioColaborador+valorAumento)

#Salarios mariores de 1500
else:
    aumentopercentual = "5%"
    valorAumento = salarioColaborador*0.05
    novoSalario= (salarioColaborador+valorAumento)

#Sáida
print(f"Salário antes do reajuste: {salarioColaborador:.2f}")
print(f"Percentual de aumento aplicado: {aumentopercentual}")
print(f"Valor do aumento: {valorAumento:.2f}")
print(f"Novo salário após o aumento: {novoSalario:.2f}")