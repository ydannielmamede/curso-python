idades = int(input("digitar idades"))
media = 0
soma = 0

while True:
    if idades<0:
        print("impossivel calcular")
        break
    if idades >0:
       soma += idades
       media += 1
       idades = int(input("digitar idades"))   
    else:
        break
print(media/soma)