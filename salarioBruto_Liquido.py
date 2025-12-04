nome = input("Inserir nome: ")
valorPorHora = float(input("Inserir valor recebido por hora: "))
horasTrabalhadas = float(input("Inserir horas trabalhadas: "))

pagamentoBruto = valorPorHora * horasTrabalhadas
pagamentoLiquido = pagamentoBruto - (pagamentoBruto * 0.075)

print(f"Pagamento bruto: {pagamentoBruto}")
print(f"pagamento liquido: {pagamentoLiquido}")
