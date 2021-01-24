lista = ['Artur', 'Teste', 1, 2, 3, 4]

print(lista.index('Artur'))
print(lista.index('Teste'))
print(lista.index(4))
print(2 in lista)

if 5 in lista:
    print('tá')
else:
    print('n tá')

print(lista[::-1])
del lista[5]
lista.reverse()
