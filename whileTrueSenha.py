senha = int(2002)
digitarSenha = int(input("Digitar senha: "))
tentativas = 1
while True:
    if digitarSenha != senha:
        digitarSenha = int(
            input(f"Senha incorreta, digitar novamente: {3-tentativas} restante(s): ")
        )
        tentativas += 1
    else:
        print("Senha correta!")
        break

    if tentativas == 3 and digitarSenha != 2002:
        print("Limite excedido")
        break
