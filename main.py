menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

if __name__ == '__main__':
    while True:
        print(menu)
        opcao = input("=>")

        if opcao == 'd':
            valor_deposito = float(input("Insira o Valor para depósito: "))
            if valor_deposito <= 0:
                print("=========================== FALHA ===========================")
                print(f"Valor {valor_deposito:.2f} inválido para conta.")
                print("=============================================================")
                continue
            saldo += valor_deposito
            extrato += f'+ Depósito de R${valor_deposito:.2f}\n'
            print("=========================== SUCESSO ===========================")
            print(f"Depósito de R${valor_deposito:.2f} na sua conta.")
            print("===============================================================")

        elif opcao == 's':
            valor_saque = float(input("Insira o Valor para saque: "))
            if numero_saques >= LIMITE_SAQUES:
                print("=========================== FALHA ===========================")
                print(f"Limite de 3 Saques alcançado, Tente Amanhã")
                print("=============================================================")
                continue
            if valor_saque > limite:
                print("=========================== FALHA ===========================")
                print(f"Valor de saque ultrapassou o limite de R${limite:.2f}")
                print("=============================================================")
                continue
            if valor_saque > saldo:
                print("=========================== FALHA ===========================")
                print(f"Valor de Saque inválido, saldo insuficiente.")
                print("=============================================================")
                continue
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'- Saque de R${valor_saque:.2f}\n'
            print("=========================== SUCESSO ===========================")
            print(f"Saque de R${valor_saque:.2f} na sua conta.")
            print("===============================================================")

        elif opcao == 'e':
            print("=========================== EXTRATO ===========================")
            print(f'{"Não foram realizados movimentos na conta." if not extrato else extrato}')
            print(f"Saldo: R${saldo:.2f}")
            print("===============================================================")

        elif opcao == 'q':
            break
        else:
            print("Opção inválida, Tente novamente.")
