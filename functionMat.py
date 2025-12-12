def Fatorial(x):
    for i in range(1,x-1,):
        x += x*i
    if x<=0:
        return "Não foi possivel calcular o fatorial"
    else:
        return x

def Primo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def JurosComposto(capital,taxa,tempo):
    montante = capital*((1+taxa)**tempo)
    return montante

