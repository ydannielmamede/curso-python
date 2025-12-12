import random

numero = int(input("Digitar um número: "))


def ehPrimo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


primo = ehPrimo(numero)

if primo == True:
    numeroSecreto = random.randrange(1, 21)
    print("O número é primo, o número secreto está entre 1 e 20")
else:
    numeroSecreto = random.randrange(30, 51)
    print("O número nao é primo, o número secreto está entre 30 e 50")

adivinhacao = int(input("Tente adivinhar o número secreto: "))
tentativas = 1

while True:
    if adivinhacao > numeroSecreto:
        print("Mais baixo!")
        tentativas += 1
        adivinhacao = int(input("Tente adivinhar novamente o número secreto: "))
    elif adivinhacao < numeroSecreto:
        print("Mais alto!")
        tentativas += 1
        adivinhacao = int(input("Tente adivinhar novamente o número secreto: "))
    else:
        print("Acertou!!!!")
        break

if tentativas <= 10:
    print(f"Ótimo trabalho, conseguiu em {tentativas} tentativas")
else:
    print(
        f"Demorou demais, conseguiu em {tentativas} tentativas tente ser mais rapido na próxima")
