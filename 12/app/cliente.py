from typing import List
from .pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade=idade)
        self.compras = []

    def registrar_compra(self, *args):
        self.compras.append(str('args'))

    def total_compras(self):
        for item in self.compras:
            return item

