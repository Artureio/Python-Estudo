compras = (
    {'quantidade': 2, 'valor': 20},
    {'quantidade': 3, 'valor': 30},
    {'quantidade': 40, 'valor': 2}
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['valor'], compras
    )
)
print('precos totais:', totais)
print('Total geral: ', sum(totais))
