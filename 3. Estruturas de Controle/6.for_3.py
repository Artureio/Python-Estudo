# percorrendo DICIONÁRIO \/
produto = {'nome': 'Caneta', 'preço': 15.00,
           'importada': True, 'estoque': 23}

# a chave do produto é exibida por padrão
for chave in produto:
    print(chave)

# .values() puxa somente os valores do dicionário
for valor in produto.values():
    print(valor)

# .items() puxa a chave e o valor e delega as duas variaveis
for chave, valor in produto.items():
    print(chave, valor)

# as variaveis continuam com o ultimo valor armazenado dentro do for
# ex:
print(chave, valor)
