# listar todos os meses com 31 dias(JEITO CERTO)
from functools import reduce
from locale import LC_ALL, setlocale
from calendar import mdays, month_name

setlocale(LC_ALL, 'pt_BR')

# 1- FILTER: pegar os indices com 31
# 2- MAP: atribuir os meses aos nomes dos meses
# 3- REDUCE: juntar tudo

meses_indices = filter(lambda mes: mdays[mes] == 31, range(1, 13))
indice_nomes = map(lambda t: f'{month_name[t]}', meses_indices)
juntar = reduce(
    lambda todos, nome_mes: f'{todos}\n-{nome_mes}', indice_nomes,
    'Meses com 31 dias:')

print(juntar)

# forma de fazer tudo de uma vez
print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n-{nome_mes}',
        map(
            lambda t: f'{month_name[t]}',
            filter(lambda mes: mdays[mes] == 31, range(1, 13))
        ), 'Meses com 31 dias'
    )
)
