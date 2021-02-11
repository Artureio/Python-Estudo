from functools import reduce

pessoas = (
    {'nome': 'Pedro', 'idade': 14},
    {'nome': 'Mariana', 'idade': 15},
    {'nome': 'Artur', 'idade': 18},
    {'nome': 'Elaine', 'idade': 21},
    {'nome': 'Joao', 'idade': 21},
    {'nome': 'Maria', 'idade': 52},
    {'nome': 'Thiago', 'idade': 74},
    {'nome': 'Angela', 'idade': 11},
    {'nome': 'Vitor', 'idade': 10}
)

so_idade_MAP = map(lambda i: i['idade'], pessoas)

menores_FILTER = filter(lambda i: i < 18, so_idade_MAP)

soma_idade_REDUCE = reduce(lambda idades, p: idades + p, menores_FILTER, 0)

print(soma_idade_REDUCE)
