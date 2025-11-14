extrato = ""
LIMITE_SAQUE = 4
saldo  = 0
contagem = 0
i, e = 1, 1
print("\n", "Sistema Bancario".center(25))
while True:
    print("[1] Deposito\n[2] Saque\n[3] Extrato\n[0] Sair")
    opcao = int(input("Escolha uma opção valida: "))
    if opcao > 3 or opcao < 0:
        print("Opcao invalida!")
        continue
    elif(opcao == 1):
        print("\n", "Deposito".center(25))
        while True:
            valor = int(input("digite o valor: "))
            if valor < 1:
                print("Deposito invalido\nTente novamente:")
                i+=1
                if i == 3:
                    print()
                    break
            else:
                saldo+= valor
                extrato+= f"\nDeposito:R$ {valor}"
                print(f"Deposito de {valor} feito com sucesso!\n")
                break
    elif(opcao == 2):
        print("\n", "Saque".center(25))
        for i in range(2):
            saque = int(input("Digite o valor de saque: "))
            if saque > saldo:
                print("Não tens Saldo suficiente!")
                if i == 1:
                    print()
            elif(saque<=0):
                print("saldo invalido!")
                e+1
                if e == 3:
                    print()
                    break
            else:
                contagem+=1
                if contagem == LIMITE_SAQUE:
                    print("Antigio o limite de saque!\n")
                else:
                    saldo-=saque
                    extrato+= f"\nSaque:R$ {saque}"
                    print(f"Saque de {saque} feito com sucesso!\n")

                break
    elif(opcao == 3):
        print("\n", "Extrato".center(25))
        if extrato == "":
            print("Nenhuma movimentacao feita\n")
        else:
            print(extrato)
            print(f"Saldo total: R$ {saldo}\n")

    elif(opcao == 0):
        print("ENCERADO!\n")
        break

        




