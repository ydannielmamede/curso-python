numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

while numero1 != numero2:
    if numero1 < numero2:
        print("crescente")
    else:
        print("decrescente")
    
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
print("Números iguais. Fim do programa.")
    
