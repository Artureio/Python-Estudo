MaiorIdade = 18


class Pessoa(object):
    def __init__(self, nome, idade=None):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome
        return f'{self.nome} ({self.idade} anos)'

    def isAdult(self):
        return (self.idade or 0) > MaiorIdade
