def deposito(saldo_atual, extrato_atual,/):
    deposito = float(input(f'Valor a ser Depositado:'))

    if (deposito > 0):
        saldo_atual += deposito
        extrato_atual += f"""  Deposito - R${deposito:.2f} \n"""
        print(f'Deposito - R${deposito:.2f} realizado com sucesso')
        return saldo_atual, extrato_atual
    else:
        print(f'Deposito inválido')
        return saldo_atual, extrato_atual


def saque(*,saldo_atual, extrato_atual, numero_de_saques, limite_de_saques):
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


def verifica_extrato(saldo_atual,/,*, extrato):
    print(f'\n    ## EXTRATO ##   ')
    print(extrato)
    print(f'Saldo - R${saldo_atual:.2f}')


def cadastra_usuario(usuarios_atual):
    usuario = {}
    
    nome = input("Entre com o nome: ")
    usuario["nome"] = nome
    data_de_nasc = input("Entre com a data de nescimento: ")
    usuario["data de nascimento"] = data_de_nasc
    cpf = int(input("Entre com o CPF: "))
    
    for usuario in usuarios_atual:
        print(usuario["cpf"])
        if usuario["cpf"] == cpf:
            print("Esse cpf já está cadastrado")
            return usuarios_atual
    
    usuario["cpf"] = cpf
    endereço = """"""
    logadouro = input("Entre com  o Logadouro: ")
    bairro = input("Entre com  o Bairro: ")
    cidade = input("Entre com  a Cidade: ")
    estado = input("Entre com  o Estado: ")
    endereço += f"""Logadouro - {logadouro}, bairro {bairro}, cidade = {cidade}, estado - {estado}"""
    usuario["endereço"] = endereço
    usuarios_atual.append(usuario)
    
    return usuarios_atual


def mostra_usuarios(usuarios_atual):
    for usuario in usuarios_atual:
        for chave, valor in usuario.items():
            print(f'{chave} - {valor}')
        print('\n')


def cadastra_conta(contas_atual, usuarios_atual):
    conta = {}
    conta["agencia"] = "0001"
    
    if len(contas_atual) == 0:
        conta["numero da conta"] = 1
    else:
        ultima_conta = contas_atual[len(contas_atual) - 1]
        conta["numero da conta"] = ultima_conta["numero da conta"] + 1
    
    cpf = int(input("Entre com o CPF: "))
    flag_cpf = True
    for usuario in usuarios_atual:
        
        if usuario["cpf"] == cpf:
            flag_cpf = False
            break
        
    if flag_cpf == True:
        print(f'CPF não cadastrado cadastre o usuario primeiro')
        return contas_atual
    else:
        conta["cpf"] = cpf
        contas_atual.append(conta)
        return contas_atual


def mostra_contas(contas_atual):
    for conta in contas_atual:
        for chave, valor in conta.items():
            print(f'{chave} - {valor}')
        print('\n')


menu = """
        ### Menu ###
    
    (1) - Depositar
    (2) - Sacar
    (3) - Extrato
    (4) - Cadastra Usuario
    (5) - Mostra Usuarios
    (6) - Cadastra Conta
    (7) - Mostra Conta
    (8) - Sair

"""

saldo = 0
extrato = """"""
num_de_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500
usuarios = []
contas = []


while True:
    opcao = int(input(menu))

    if opcao == 1:
        saldo, extrato = deposito(saldo,extrato)

    elif opcao == 2:
        saldo, extrato, num_de_saques = saque(saldo_atual=saldo, extrato_atual=extrato, numero_de_saques=num_de_saques, limite_de_saques=LIMITE_SAQUES)

    elif opcao == 3 :
        verifica_extrato(saldo, extrato=extrato)
    
    elif opcao == 4 :
        usuarios = cadastra_usuario(usuarios)
        
    elif opcao == 5 :
        mostra_usuarios(usuarios)
    
    elif opcao == 6 :
        contas = cadastra_conta(contas, usuarios)
    
    elif opcao == 7 :
        mostra_contas(contas)
    
    elif opcao == 8 :
        print(f'Saldo - R${saldo:.2f}')
        break
    else:
        print("Opção invalida")