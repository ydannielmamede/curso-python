valorDisponivel = 1000
valorSaque = float(input("Digitar valor do saque: "))

if valorSaque > valorDisponivel:
    print("Saldo indiponível")
else:
    print(f"\nValor sacado: R${valorSaque:.2f}\nNovo saldo disponível: R${valorDisponivel-valorSaque:.2f}\n")