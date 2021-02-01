class Humano:
    # atributo de classe
    especie = 'homo sapiens'

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Nome: {self.nome}\nEspecie: {self.especie}'
        
    def das_cavernas(self):
        self.especie = 'homo neanderthalensis'
        # return self permite encadear funções logo após a criação da instancia
        return self


if __name__ == '__main__':
    marcelo = Humano('marcelo')
    shrek = Humano('shrek').das_cavernas()
    
    print(marcelo)
    print(shrek)
