
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tar for tar in self.tarefas if tar.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:

    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('  (Concluido)  ')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Expirado)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Expira em {dias} dias)')
        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('casa')
    casa.add('passar')
    casa.add('lavar', datetime.now() + timedelta(seconds=2))
    casa.add('cozinhar',)
    casa.add('nenem')
    casa.procurar('cozinhar').concluir()
    casa.tarefas.append(TarefaRecorrente('malhar', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('malhar').concluir())

    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
