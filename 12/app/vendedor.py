from .pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade=idade)
        self.salario = salario
