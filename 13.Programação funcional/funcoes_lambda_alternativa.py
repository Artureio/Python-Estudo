compras = (
    {'quantidade': 2, 'valor': 20},
    {'quantidade': 3, 'valor': 30},
    {'quantidade': 40, 'valor': 2}
)


def total(compra):
    return compra['quantidade'] * compra['valor']


totais = tuple(map(total, compras))

print('precos totais:', totais)
print('Total geral: ', sum(totais))
