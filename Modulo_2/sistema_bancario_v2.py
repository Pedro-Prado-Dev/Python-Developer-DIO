def deposito(saldo_atual, extrato_atual):
    deposito = float(input(f'Valor a ser Depositado:'))

    if (deposito > 0):
        saldo_atual += deposito
        extrato_atual += f"""  Deposito - R${deposito:.2f} \n"""
        print(f'Deposito - R${deposito:.2f} realizado com sucesso')
        return saldo_atual, extrato_atual
    else:
        print(f'Deposito inválido')
        return saldo_atual, extrato_atual

def saque(saldo_atual, extrato_atual, numero_de_saques, limite_de_saques):
    saque = float(input(f'Valor a ser Sacado:'))

    if saque <= saldo and num_de_saques < LIMITE_SAQUES and saque <= LIMITE:
        saldo_atual -= saque
        numero_de_saques += 1
        extrato_atual += f"""  Saque - R${saque:.2f} \n"""
        print(f'Saque - R${saque:.2f} realizado com sucesso')

        return saldo_atual, extrato_atual, numero_de_saques

    elif num_de_saques >= limite_de_saques:
        print(f'Numero de saques excedidos')
        return saldo_atual, extrato_atual, numero_de_saques

    elif saque > LIMITE:
        print(f'Saque maior que o limite permitido de R$500.00')
        return saldo_atual, extrato_atual, numero_de_saques

def verifica_extrato(extrato):
    print(f'\n    ## EXTRATO ##   ')
    print(extrato)
    print(f'Saldo - R${saldo:.2f}')


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
        saldo, extrato = deposito(saldo_atual=saldo, extrato_atual=extrato)

    elif opcao == 2:
        saldo, extrato, num_de_saques = saque(saldo_atual=saldo, extrato_atual=extrato, numero_de_saques=num_de_saques, limite_de_saques=LIMITE_SAQUES)

    elif opcao == 3 :
        verifica_extrato(extrato)

    elif opcao == 4 :
        print(f'Saldo - R${saldo:.2f}')
        break
    else:
        print("Opção invalida")