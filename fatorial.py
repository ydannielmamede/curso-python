numero = int(input("Calcular fatoria do número: "))


def fatorial(x):
    for i in range(1,x-1,):
        x += x*i
    if x<=0:
        print("Não foi possivel calcular o fatorial")
    else:
        print(x)

fatorial(numero)
