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
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo :
            print(f"\n Falha! Seu saldo é insuficiente")
        
        elif valor > 0:
            self._saldo += valor
            print(f"\n Saque no valor R${valor} realizado com sucesso")
        
        else:
            print(f" Valor informado para saque invalido")

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