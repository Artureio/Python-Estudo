pessoa = {'nome': 'Artur', 'idade': '26', 'cursos': [
    'ingles', 'sistemas de informação', 'analista de dados']}

print(pessoa['nome'])
print(pessoa['cursos'])
print(pessoa['idade'])
print(len(pessoa))

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

# adicionar valor
pessoa['cursos'].append('angular')

for a in pessoa:
    print(a, ':', pessoa[a])
