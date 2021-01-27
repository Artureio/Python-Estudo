
from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tar for tar in self.tarefas if tar.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:

    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida) ' if self.feito else '')


def main():
    casa = Projeto('casa')
    casa.add('passar')
    casa.add('lavar')
    casa.add('cozinhar')
    casa.add('nenem')
    casa.procurar('cozinhar').concluir()

    for tarefa in casa.tarefas:
        print(f'- {tarefa}')

    mercado = Projeto('mercado')
    mercado.add('tomate')
    mercado.add('salsa')
    mercado.add('cebola')
    mercado.procurar('cebola').concluir()


if __name__ == '__main__':
    main()
