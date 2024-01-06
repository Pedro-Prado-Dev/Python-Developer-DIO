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
            return True
        else:
            print(f" Valor informado para saque invalido")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n Deposito de R${valor} realizado com sucesso !!")
            return True
        else:
            print(f"Deposito com valor inválido")
            return False
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques=3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques= limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor >self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print(f" Operações invalida, excedeu seu 
                  limite")
        
        elif excedeu_saques:
            print(f"Operação invalida, você usou seu limite
                  de saques")
        
        else:
            print(f"Sacou R${valor}")
            return super().sacar(valor)
        
        return False
    
    def __str__(self) -> str:
        return f"""\
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """          

class Historico:
    def __init__(self) -> None:
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacoes(self, transacao):
        self._transacoes.append(
            {
                "tipo":transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass