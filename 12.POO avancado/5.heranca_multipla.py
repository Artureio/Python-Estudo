class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('falar', 'pensar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('teia', 'andar pela parede')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandido',)


if __name__ == '__main__':
    animal = Animal()
    pedro = Homem()
    tarantula = Aranha()
    omiranha = HomemAranha()

    print(f'animal: {animal.capacidades}')
    print(f'Pedro: {pedro.capacidades}')
    print(f'tarantula: {tarantula.capacidades}')
    print(f'O Miranha: {omiranha.capacidades}')
