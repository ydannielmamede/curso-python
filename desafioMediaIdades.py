idades = int(input("Digitar idades: "))
media = 0
soma = 0
while True:
    if idades > 0:
        soma += idades
        media += 1
        idades = int(input("Digitar idades: "))
    else:
        break
if media == 0:
    print("Impossível calcular")
else:
    print(soma / media)
