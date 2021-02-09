class Humano:
    # atributo de classe
    especie = 'homo sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um numero positivo')
        self._idade = idade

    def __str__(self):
        return f'Nome: {self.nome}\nEspecie: {self.especie}'
    # método de instancia: recebe o SELF como parametro

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        # return self permite encadear funções logo após a criação da instancia
        return self

    # método estático(não recebe parâmetro)
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # metodo de classe(recebe uma classe como parametro)
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':

    jose = HomoSapiens('jose')
    jose.idade = 50
    print(f'nome: {jose.nome} Idade: {jose.idade}')
