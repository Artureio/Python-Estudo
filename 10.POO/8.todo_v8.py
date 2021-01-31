
from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        try:
            return [tarefa for tarefa in self.tarefas if not tarefa.feito]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

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
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)

        if self.dono:
            self.dono += nova_tarefa


def main():
    casa = Projeto('casa')
    casa.add('passar')
    casa.add('lavar', datetime.now() + timedelta(seconds=2))
    casa.add('cozinhar',)
    casa.add('nenem')
    casa.procurar('cozinhar').concluir()
    casa += TarefaRecorrente('malhar', datetime.now(), 7)
    casa.procurar('malhar').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
