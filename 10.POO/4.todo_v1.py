from datetime import datetime


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
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))
    casa.append(Tarefa('Arrumar nenem'))
    casa.append(Tarefa('Estudar'))

    # desafio: Percorrer a lista e aplicar o método Concluir em lavar prato
    # list comprehension para aplicar o método
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    # laço for para imprimir
    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
