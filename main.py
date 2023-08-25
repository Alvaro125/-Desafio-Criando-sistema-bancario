import textwrap
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f'+ Depósito de R${valor:.2f}\n'
        print("=========================== SUCESSO ===========================")
        print(f"Depósito de R${valor:.2f} na sua conta.")
        print("===============================================================")
    else:
        print("=========================== FALHA ===========================")
        print(f"Valor {valor:.2f} inválido para conta.")
        print("=============================================================")
    return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("=========================== FALHA ===========================")
        print(f"Limite de 3 Saques alcançado, Tente Amanhã")
        print("=============================================================")
    elif valor > limite:
        print("=========================== FALHA ===========================")
        print(f"Valor de saque ultrapassou o limite de R${limite:.2f}")
        print("=============================================================")
    elif valor > saldo:
        print("=========================== FALHA ===========================")
        print(f"Valor de Saque inválido, saldo insuficiente.")
        print("=============================================================")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f'- Saque de R${valor:.2f}\n'
        print("=========================== SUCESSO ===========================")
        print(f"Saque de R${valor:.2f} na sua conta.")
        print("===============================================================")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("=========================== EXTRATO ===========================")
    print(f'{"Não foram realizados movimentos na conta." if not extrato else extrato}')
    print(f"Saldo: R${saldo:.2f}")
    print("===============================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=========================== FALHA ===========================")
        print(f"+++++++++++++++Já existe Usuario com esse CPF!+++++++++++++++")
        print("=============================================================")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=========================== SUCESSO ===========================")
    print(f"+++++++++++++++++ Usuário criado com sucesso! +++++++++++++++++")
    print("===============================================================")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=========================== SUCESSO ===========================")
        print(f"++++++++++++++++++ Conta criada com sucesso! ++++++++++++++++++")
        print("===============================================================")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("=========================== FALHA ===========================")
    print(f"Usuário não encontrado, fluxo de criação de conta encerrado!")
    print("=============================================================")
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
