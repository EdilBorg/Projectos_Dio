from datetime import datetime  

def criar_usuario(*, dados):
    print(("\ncriar conta".title()).center(30))
    dados["Nome"] = input("Nome: ")
    if type(dados) == list:
        novo = {}
        dados.append(novo)
        dados = novo
    while True:
        dados["Data_Nascimento"] = input("Data de Nascimento (Data/Mes/Ano): ")
        d, m, a = dados["Data_Nascimento"].split("/")
        dia, mes, ano = int(d), int(m), int(a)

        if (mes == 2):
            if dia > 29:
                print("Data invalido")
                continue
        elif (dia < 1 or dia > 31):
            print("Data invalida!")
            continue
        elif (mes < 1 or mes > 12):
            print("mes invalido!")
            continue
        elif (ano > 2025 or ano < 1900):
            print("Ano invalido!")
            continue
        else:
            dados["CPF"] = int(input("CPF: "))
            for u in usuario:
                if u["CPF"] == dados["CPF"]:
                    print("Já existe uma conta com este CPF!")
                    del dados["CPF"]
                    break
            print("Endereço:")
            dados["Endereco"] = input("logradouro, nro - bairro - cidade/sigla estado: ")
            break
    usuario.append(dados)
    print("Usuario cadastrado com sucesso\n")
    return 1, dados["Nome"]

def conta(nr_contas):
    informacao = {}
    nr, info = criar_usuario(dados=informacao)
    if len(usuario) > 0:
        for u in usuario:
            if "CPF" in informacao and u["CPF"] == informacao["CPF"]:
                print("Conta corrente NÃO pode ter o mesmo CPF da conta principal!\n")
                return 0
    informacao["Agencia"] = "0001"
    informacao["numero_conta"] = nr_contas + nr
    informacao["usuario"] = info
    return nr_contas + nr

def deposito(nr_contas, transacoes):
    print(("deposito".title()).center(30))
    if transacoes >= 10: 
        print("Você excedeu o número de transações permitidas para hoje!\n")
        return 0, "", 0

    while True:
        if nr_contas > 1:
            verificar_conta = int(input("Digite o numero da conta: "))
            if verificar_conta > nr_contas or verificar_conta <= 0:
                print(f"A conta {verificar_conta} não existe!")
                continue
        valor = float(input("Digite o valor: "))
        if valor <= 0:
            print("Valor invalido!")
            continue
        else:
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  
            extra = f"\n{agora} - Deposito: R$ {valor:.2f}"
            if nr_contas > 1:
                print(f"Deposito de {valor} feito com sucesso na conta {verificar_conta}\n")
                return valor, extra, 1
            else:
                print(f"Deposito de {valor} feito com sucesso\n")
                return valor, extra, 1

def saque(*, salde, LIMITE_SAQU, f, transacoes):
    print(("saque".title()).center(30))
    if transacoes >= 10: 
        print("Você excedeu o número de transações permitidas para hoje!\n")
        return 0, "", 0
    while True:
        if f >= LIMITE_SAQU:
            print("Atingio o limite de saque de hoje\n")
            return 0, "", 0
        else:
            dinheiro = float(input("Digite o valor: "))
            if salde < dinheiro or dinheiro <= 0:
                print("Valor invalido\n")
                return 0, "", 0
            else:
                f += 1
                agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
                soma_dinheiro = salde - dinheiro
                extracte = f"\n{agora} - Saque: R$ {dinheiro}"
                print(f"Saque de {dinheiro} feito com sucesso\n")
                return soma_dinheiro, extracte, f, 1

def extracto(saldo, *, extrat):
    print(("Extrato".title()).center(30))
    print(extrat)
    print(f"Saldo total: R$ {saldo}\n")

LIMITE_SAQUE = 4
extrato = ""
saldo = 0
i = 0
transacoes = 0  
usuario = []
nr_contas = 0

while True:
    print("\n", "Sistema Bancario.v2".center(25))
    print("[1]-Criar usuário\n[2]-Criar conta corrente\n[3]-Deposito\n[4]-Saque\n[5]-Extrato\n[0]-Sair".title())
    opcao = int(input("Escolha uma opção valida: "))

    if opcao == 1:
        print()
        criar_usuario(dados={})
    elif opcao == 2:
        e = conta(nr_contas)
        nr_contas += e
    elif opcao == 3:
        print()
        sald, extra, t = deposito(nr_contas, transacoes)
        if t != 0:
            saldo += sald
            extrato += extra
            transacoes += t
    elif opcao == 4:
        print()
        dinheiro_soma, extrado, e, t = saque(salde=saldo, LIMITE_SAQU=LIMITE_SAQUE, f=i, transacoes=transacoes)
        if t != 0:
            saldo = dinheiro_soma
            i += e
            transacoes += t
            extrato += extrado
    elif opcao == 5:
        print()
        extracto(saldo, extrat=extrato)
    elif opcao > 5:
        print("Opcao invalida!\n")
    elif opcao == 0:
        print("Encerado")
        break
