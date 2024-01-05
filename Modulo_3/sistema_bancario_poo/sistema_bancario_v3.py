from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self,nome, data_nascimeto, cpf, endereco) -> None:
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimeto
        self.cpf = cpf

class Conta:
    pass

class ContaCorrente(Conta):
    pass

class Historico:
    pass

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass