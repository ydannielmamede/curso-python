import random 
numero = random.randrange(1,101)
palpite = 1
meu_palpite = int(input("Digite um número entre 1 e 100: "))
while meu_palpite != numero:
    palpite += 1
    if meu_palpite > numero:
        print(meu_palpite,"é maior que o número secreto.")
        meu_palpite = int(input("Digite outro número entre 1 e 100: "))
    elif meu_palpite < numero:
        print(meu_palpite,"é menor que o número secreto.")
        meu_palpite = int(input("Digite outro número entre 1 e 100: "))
print("Parabéns! Você acertou o número secreto", numero, "em", palpite, "tentativas.")