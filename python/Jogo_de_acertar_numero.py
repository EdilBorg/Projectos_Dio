from getpass import getpass
i, e= 0, 3
ponto1, ponto2 = 0, 0
nome_1jogador = input("Nome do 1° Jogador: ")
nome_2jogador = input("Nome do 2° Jogador: ")
while True:
    if i == 0:
        print("\n_________________________________________________________________________________")
        numero_escolhodo1 = int(getpass(f"|{nome_1jogador.upper()}| Digite um numero de 0 a 10: "))
        i+=1
    elif i < 4:
        print(f"\n====== {e} Tentativas ======")
        tentativa2 = int(input(f"Digite o numero escolhido por |{nome_1jogador.upper()}|: "))
        e-=1
        i+=1
        if tentativa2 == numero_escolhodo1:
            ponto2+=1
            print("CERTO!")
            i-=1
            continue
        else:
            print("ERRADO!")
            print(f" o valor de i: {i}")
        if e == 0:
            e+=3
    elif i == 4:
        print("\n_______________________________________________________________________________")
        numero_escolhodo2 = int(getpass(f"|{nome_2jogador.upper()}| Digite um numero de 0 a 10: "))
    elif i > 6 and i<9:
        print(f"====== {e} Tentativas ======")
        tentativa1 = int(input(f"Digite o numero escolhido por |{nome_2jogador.upper()}|: "))
        e-=1
        if tentativa2 == numero_escolhodo1:
            ponto1+=1
            print("CERTO!")
            i-=1
            continue
        else:
            print("ERRADO!")
            print(f" o valor de i: {i}")

    elif i == 9:
        print("\n___________________________________________________________________________")
        print("[1] Continuar\n[2] sair")
        opcao = int(input("Escolha uma opcão valida: "))
        if opcao == 1:
            i-=9
            e-=3
            continue
        else:
            print("ENCERADO!")
            break