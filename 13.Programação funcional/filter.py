pessoas = [
    {'nome': 'Pedro', 'idade': 14},
    {'nome': 'Mariana', 'idade': 15},
    {'nome': 'Artur', 'idade': 18},
    {'nome': 'Elaine', 'idade': 21},
    {'nome': 'Joao', 'idade': 21},
    {'nome': 'Maria', 'idade': 52},
    {'nome': 'Thiago', 'idade': 74},
    {'nome': 'Angela', 'idade': 11},
    {'nome': 'Vitor', 'idade': 10}
]

menores_idade = list(filter(lambda i: i['idade'] < 18, pessoas))
print(menores_idade)
print('---------------------------------------')

# DESAFIO: mostrar apenas os nomes com menos de 6 caracteres
# utilizando FILTER

nomes_pequenos = list(filter(lambda n: len(n['nome']) <= 5, pessoas))

print(nomes_pequenos)
