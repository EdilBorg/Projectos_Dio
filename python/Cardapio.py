def mensagem(a):
    if a == 3:
        print()
        print(("Pratos Principais – Massas".upper()).center(35))
        print("[1]-Espaguete à bolonhesa – R$ 25,00\n[2]-Lasanha de carne – R$ 28,00\n[3]-Penne ao molho Alfredo – R$ 26,00\n" \
        "[4]-Ravioli de queijo com molho de tomate – R$ 27,00\n[0]-Voltar ao Menu")
    elif a == 4:
        print()
        print(("acompanhamentos".upper()).center(35))
        print("[1]-Arroz branco ou integral – R$ 8,00\n[2]-Feijão tropeiro – R$ 10,00\n[3]-Purê de batata – R$ 9,00\n" \
        "[4]-Legumes salteados – R$ 12,00\n[5]-Batatas rústicas – R$ 12,00\n[0]-Voltar ao Menu")
    elif a == 5:
        print()
        print(("saladas".upper()).center(35))
        print("[1]-Salada Caesar – R$ 18,00\n[2]-Salada de folhas verdes com frutas – R$ 16,00\n" \
        "[3]-Salada de grão-de-bico – R$ 15,00\n[4]-Salada de tomate com cebola – R$ 14,00\n[0]-Voltar ao Menu")
print()
valor = 0
pedido = [""]
print(("Cardapio do restaurante".upper()).center(40,"_"))
while True:
    print()
    print(("menu".upper()).center(29))
    print(("categorias\n".upper()).center(29))
    print("[1]-Sopa e caldos\n[2]-Pratos Principais – Carnes\n[3]-Pratos Principais – Massas\n" \
    "[4]-Acompanhamentos\n[5]-Saladas\n[6]-listar pedidos\n[0]-sair".upper())

    opcao = int(input("..Escolha uma opção valida: "))
    if opcao > 6 or opcao < 0:
        print("Opção invalida!\n")

    elif(opcao == 1):
         while True:
            print()
            print("SOPA E CALDOS".center(29))
            print("[1]-Sopa de Legumes – R$ 12,00\n[2]-Caldo Verde – R$ 14,00\n[3]-Creme de Abóbora – R$ 13,00\n"
                  "[4]-Canja de Galinha – R$ 15,00\n[0]-Voltar ao Menu")
            
            opcao1=int(input("..Escolha uma opção valida: "))
            if opcao1 > 4 or opcao1 < 0:
                print("Opção invalida!")
            elif opcao1 == 1:
                pedido.append("\nSopa de legumes – R$ 12,00")
                valor+=12
            elif opcao1 == 2:
                pedido.append("\nCaldo verde – R$ 14,00")
                valor+=14
            elif opcao1 == 3:
                pedido.append("\nCreme de abóbora – R$ 13,00")
                valor+=13
            elif opcao1 == 4:
                pedido.append("\nCanja de galinha – R$ 15,00")
                valor+=15
            elif opcao1 == 0:
                break
    elif opcao == 2:
        while True:
            print()
            print("PRATOS PRINCIPAIS – CARNES".center(35))
            print("[1]-Bife acebolado com arroz e feijão – R$ 28,00\n[2]-Frango grelhado com legumes – R$ 25,00\n" \
            "[3]-Costela ao molho barbecue – R$ 35,00\n[5]-Filé de peixe grelhado com purê de batata – R$ 32,00\n" \
            "[0]-Voltar ao Menu")
            opcao2 = int(input("..Escolha uma opção: "))

            if opcao2 > 5 or opcao2 < 0:
                print("Opção invalida!")
            elif opcao2 == 1:
                pedido.append("\nEspaguete à bolonhesa – R$ 25,00")
                valor+=28
            elif opcao2 == 2:
                pedido.append("\n")
                valor+=25
            elif opcao2 == 3:
                pedido.append("\nCostela ao molho barbecue – R$ 35,00")
                valor+=35
            elif opcao2 == 4:
                pedido.append("\nFilé de peixe grelhado com purê de batata – R$ 32,00")
                valor+=32
            elif opcao2 == 0:
                break
    elif opcao == 3:
        while True:
            mensagem(3)
            opcao3 = int(input("..Escolha uma opção: "))
            if opcao2 > 4 or opcao3 < 0:
                print("Opção invalida!")
            elif opcao3 == 1:
                pedido.append("\nBife acebolado com arroz e feijão – R$ 28,00")
                valor+=28
            elif opcao3 == 2:
                pedido.append("\nLasanha de carne – R$ 28,00")
                valor+=28
            elif opcao3== 3:
                pedido.append("\nPenne ao molho Alfredo – R$ 26,00")
                valor+=26
            elif opcao3 == 4:
                pedido.append("\nRavioli de queijo com molho de tomate – R$ 27,00")
                valor+=27
                break
            elif opcao3 == 0:
                break
    elif opcao == 4:
        while True:
            mensagem(4)
            opcao4 = int(input("..Escolha uma opção: "))
            if opcao4 > 4 or opcao4 < 0:
                print("Opção invalida!")
            elif opcao4 == 1:
                pedido.append("\nArroz branco ou integral – R$ 8,00")
                valor+=8
            elif opcao4 == 2:
                pedido.append("\nFeijão tropeiro – R$ 10,00")
                valor+=10
            elif opcao4 == 3:
                pedido.append("\nPurê de batata – R$ 9,00")
                valor+=9
            elif opcao4 == 4:
                pedido.append("\nLegumes salteados – R$ 12,00")
                valor+=12
            elif opcao4 == 5:
                pedido.append("\nBatatas rústicas – R$ 12,00")
                valor+=12
            elif opcao4 == 0:
                break
    elif opcao == 5:
        while True:
            mensagem(5)
            opcao5 = int(input("..Escolha uma opção: "))
            if opcao5 > 4 or opcao5 < 0:
                print("Opção invalida!")
            elif opcao5 == 1:
                pedido.append("\nSalada Caesar – R$ 18,00")
                valor+=18
            elif opcao5 == 2:
                pedido.append("\nSalada de folhas verdes com frutas – R$ 16,00")
                valor+=16
            elif opcao5 == 3:
                pedido.append("\nSalada de grão-de-bico – R$ 15,00")
                valor+=15
            elif opcao5 == 4:
                pedido.append("\nSalada de tomate com cebola – R$ 14,00")
                valor+=14
            elif opcao5 == 0:
                break
    elif opcao == 6:
        print("_" * 30)
        for elemento in pedido:
            print(elemento)
        print(f"total a pagar: R$ {valor}")
    elif opcao == 0:
        print("\nENCERADO!")
        break
