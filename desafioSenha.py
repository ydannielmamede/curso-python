digitarSenha = int(input("Digitar senha: "))
qualSenhaCorreta = int(input())

while digitarSenha != qualSenhaCorreta:
    digitarSenha = int(input("Senha invalida! Tente novamente: "))

print("Acesso permitido")