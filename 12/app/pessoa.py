maioridade = 18


class Pessoa(object):
    def __init__(self, nome, idade=None):
        self.nome = nome
        self.idade = idade

    def isAdult(self):
        return '( Adulto )' if self.idade >= maioridade else '( Menor )'

    def __str__(self):
        if not self.idade:
            return f'Nome: {self.nome}\n'
        return f'Nome: {self.nome} \n idade: {self.idade} {self.isAdult()}'

