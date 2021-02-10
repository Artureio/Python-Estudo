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

menores = list(filter(lambda i: i['idade'] < 18, pessoas))
print(menores)

# DESAFIO: mostrar apenas os nomes com menos de 5 caracteres
# utilizando FILTER

carac = list(filter(lambda n: len(n['nome']) <= 5, pessoas))

print(carac)
