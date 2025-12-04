senha = int(2002)
digitarsenha = int(input("digitar senha: "))
tentativas = 0
while True:
    if digitarsenha != senha:
        digitarsenha = int(input("Senha incorreta, digitar novamente: "))
        tentativas += 1
    else:
        print("Senha correta!")
        break
    
    if tentativas ==3:
        print("Limite excedido")
        break