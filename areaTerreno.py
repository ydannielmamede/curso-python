comprimento = float(input("Digite a comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
metroQuadrado = float(input("Digite o valor do metro quadrado: "))

area = comprimento * largura
preco = area * metroQuadrado

print(f"Area do terreno = {area:.2f}m²")
print(f"Preco do terreno = {preco:.2f}")
