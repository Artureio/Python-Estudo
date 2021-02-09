class Humano:
    # atributo de classe
    especie = 'homo sapiens'

    def __init__(self, nome):
        self.nome = nome

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

    marcelo = HomoSapiens('marcelo')
    shrek = Neanderthal('shrek')

    print(
        f'a evolucao(a partir da classe): {", ".join(HomoSapiens.especies())}')
    eren = Humano('Eren')
    print(f'a evolucao(a partir da instancia): {", ".join(eren.especies())}\n')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Homo Sapiens evoluido? {Neanderthal.is_evoluido()}')
    print(f'marcelo evoluido? {marcelo.is_evoluido()}')
    print(f'shrek  evoluido? {shrek.is_evoluido()}')
