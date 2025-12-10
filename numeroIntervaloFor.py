numeroQuantidade = int(input("Digitar quantos números deseja incluir: "))
dentro = 0
fora = 0

for i in range(1, (numeroQuantidade + 1)):
    x = int(input(f"Digite o {i} número: "))
    if x > 10 and x < 20:
        dentro += 1
    else:
        fora += 1

print(f"Números dentro do intervalo: {dentro}")
print(f"Números fora do intervalo: {fora}")
