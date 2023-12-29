import datetime

class Pessoa:
    def __init__(self, nome, ano_nascimento) -> None:
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = datetime.datetime.now().year
        return _ano_atual - self._ano_nascimento
    
    
pessoa = Pessoa("Pedro", 2000)
print(f'Nome : {pessoa.nome} e idade : {pessoa.idade}')
    