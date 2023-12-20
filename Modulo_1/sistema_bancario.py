menu = """
        ### Menu ###
    
    (1) - Depositar
    (2) - Sacar
    (3) - Extrato
    (4) - Sair

"""

saldo = 0
extrato = """"""
num_de_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500


while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input())

        if(deposito > 0):
            saldo += deposito
            extrato += f"""  Deposito - R${deposito:.2f} \n"""
            print(f'Deposito - R${deposito:.2f} realizado com sucesso')
        else:
            print(f'Deposito inválido')

    elif opcao == 2:
        saque = float(input())

        if saque <= saldo and num_de_saques < LIMITE_SAQUES and saque <= LIMITE:
            saldo -= saque
            num_de_saques += 1
            extrato += f"""  Saque - R${saque:.2f} \n"""
            print(f'Saque - R${saque:.2f} realizado com sucesso')

        elif num_de_saques >= LIMITE_SAQUES:
            print(f'Numero de saques excedidos')

        elif saque > LIMITE:
            print(f'Saque maior que o limite permitido de R$500.00')

    elif opcao == 3 :
        print(f'\n    ## EXTRATO ##   ')
        print(extrato)
        print(f'Saldo - R${saldo:.2f}')

    elif opcao == 4 :
        print(f'Saldo - R${saldo:.2f}')
        break
    else:
        print("Opção invalida")