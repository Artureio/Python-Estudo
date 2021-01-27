class Data:
    # Criação do construtor com atributos padrões
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    # Método __str__  converte o objeto para string  de forma implicita

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d2 = Data(21, 8, 1995)
print(d1)
print(d2)
