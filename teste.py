import functionMat

numero = int(input("numeroo"))
taxa = float(input("taxa : "))
tempo = int(input("meses: "))

primo = functionMat.Primo(numero)
fatorial = functionMat.Fatorial(numero)
juros = functionMat.JurosComposto(numero,taxa,tempo)

print(primo)
print(fatorial)
print (juros)
