list1 = [1, 2, 3]
dobro = tuple(map(lambda x: x*2, list1))
print(dobro)

lista2 = (
    {'Nome': 'Artur', 'Idade': 22},
    {'Nome': 'Pedro', 'Idade': 30},
    {'Nome': 'Joao', 'Idade': 52},
    {'Nome': 'Andre', 'Idade': 34}
)
nomes = tuple(map(lambda nome: nome['Nome'], lista2))
print(nomes)
idades = tuple(map(lambda idade: idade['Idade'], lista2))
print(idades)

# desafio: exibir a lista 2 no seguinte formato usando o map:
# <nome> tem <anos> anos.

formatado = list(
    map(
        lambda total: f'{total["Nome"]} tem {total["Idade"]} anos',
        lista2
    )
)
print(formatado)
