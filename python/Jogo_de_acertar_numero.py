from getpass import getpass
def inicio(jogador, nome, ponto=0):
    print(("inicio do jogo".upper()).center(30,"_"))
    print()
    for i in range(3):
        valor= int(getpass(f"|{jogador.upper()}| escolha 1 numero de 1 a 10: "))
        if valor > 10:
            print("numero invalido!")
            i-=1
            continue
        print((f".{i+1}° tentativa".title()).center(30,"_"))
        tentativa = int(input(f"..|{nome.upper()}| Digite o numero escolido por |{jogador.upper()}|: "))
        if tentativa == valor:
            print(" (certo! +1 ponto)\n".upper())
            ponto+=1
        else:
            print(f" (errado!)\n (numero corecto: {valor})\n".upper())
    print(f"\nponto de |{nome.upper()}| : {ponto}\n")
         
nome_1jogador = input("Nome do 1° Jogador: ")
nome_2jogador = input("Nome do 2° Jogador: ")
while True:
    print("[1] continuar\n[2] sair".upper())
    op = int(input("Escolha uma opcao: "))
    if op == 2:
        print("ENCERADO")
        break
    elif(op == 1):
        inicio(nome_1jogador, nome_2jogador)   
        inicio(nome_2jogador, nome_1jogador)
    else:
        print("Opção invalida!\n")
        