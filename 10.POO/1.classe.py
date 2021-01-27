class Data:
    def data_format(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    # Método __str__  converte o objeto para string  de forma implicita
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()

d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1.data_format())


d2 = Data()
d2.dia = 56
d2.mes = 49
d2.ano = 99939496
print(d2)
