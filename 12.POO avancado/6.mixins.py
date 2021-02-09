class HtmlToStringMixin(object):
    def __str__(self):
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal(object):
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    artur = Pessoa('Artur Henrique')
    print(artur)
    theo = PessoaHtml('theo Filho')
    print(theo)
    toto = AnimalHtml('Toto')
    print(toto)
