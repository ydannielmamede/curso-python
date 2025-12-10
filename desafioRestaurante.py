capacidade = int(input("Informe a capacidade máxima do restaurante: "))
clientes = 0

while True:
    print("\n1. Registrar chegada de clientes")
    print("2. Verificar se o restaurante está lotado")
    print("3. Registrar saída de clientes")
    print("4. sair\n")
    menu = int(input("Escolha uma opção: "))

    if menu == 1:
        clientesnovos = int(input("Informe o número de clientes que chegaram: "))
        clientes += clientesnovos
        if clientes > capacidade:
            print("Não há lugares suficiente")
    elif menu == 2:
        if clientes >= capacidade:
            print("Restaurante lotado!")
        else:
            print(f"{capacidade-clientes} vagas disponíveis")
    elif menu == 3:
        clientessairam = int(input("Informe o número de clientes que sairam: "))
        clientes -= clientessairam
    elif menu == 4:
        break
    else:
        print("\nInformar um valor de 1 a 4!!\n")
