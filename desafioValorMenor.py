valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
    print(f"O Primeiro valor é menor: {valor1}")
elif valor2 < valor1 and valor2 < valor3:
    print(f"O Segundo valor é o menor: {valor2}")
else:
    print(f"O Terceiro valor é o menor: {valor3}")
