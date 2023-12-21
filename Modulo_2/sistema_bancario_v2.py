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

def cadastra_usuario(usuarios):
    usuario = {}
    
    nome = input("Entre com o nome: ")
    usuario["nome"] = nome
    data_de_nasc = input("Entre com a data de nescimento: ")
    usuario["data de nascimento"] = data_de_nasc
    cpf = int(input("Entre com o cpf: "))
    
    for usuario in usuarios:
        print(usuario["cpf"])
        if usuario["cpf"] == cpf:
            print("Esse cpf já está cadastrado")
            return usuarios
    
    usuario["cpf"] = cpf
    endereço = """"""
    logadouro = input("Entre com  o Logadouro: ")
    bairro = input("Entre com  o Bairro: ")
    cidade = input("Entre com  a cidade: ")
    estado = input("Entre com  o Estado: ")
    endereço += f"""Logadouro - {logadouro}, bairro {bairro}, cidade = {cidade}, estado - {estado}"""
    usuario["endereço"] = endereço
    usuarios.append(usuario)
    
    

menu = """
        ### Menu ###
    
    (1) - Depositar
    (2) - Sacar
    (3) - Extrato
    (4) - Cadastra Usuario
    (6) - Sair

"""

saldo = 0
extrato = """"""
num_de_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500
usuarios = []


while True:
    opcao = int(input(menu))

    if opcao == 1:
        saldo, extrato = deposito(saldo,extrato)

    elif opcao == 2:
        saldo, extrato, num_de_saques = saque(saldo_atual=saldo, extrato_atual=extrato, numero_de_saques=num_de_saques, limite_de_saques=LIMITE_SAQUES)

    elif opcao == 3 :
        verifica_extrato(saldo, extrato=extrato)
    
    elif opcao == 4 :
        cadastra_usuario(usuarios)
        print(usuarios)

    elif opcao == 6 :
        print(f'Saldo - R${saldo:.2f}')
        break
    else:
        print("Opção invalida")