palavra = 'teste'
#percorrendo STRING \/
for letra in palavra:
    print(letra, end=' ')
print('\n')

#percorrendo LISTA  \/
aprovados = ['rafaela', 'teste1', 'pedro', 'artur']
aprovados2 = ['rafaela', 'teste1', 'pedro', 'artur']
aprovados3 = ['rafaela', 'teste1', 'pedro', 'artur']

for posicao, nome in enumerate(aprovados):
    print(f'{posicao})', nome, end=' ')
print('\n')

    # outra forma de fazer a mesma coisa do código acima
for nome in aprovados2:
    print(f'{aprovados2.index(nome)})', nome, end=', ')
print('\n')

    #forma mais prática 'range(len())'   
for nome in range(len(aprovados3)):
    print(f'{nome}) {aprovados3[nome]}',end=', ')
print('\n')

#percorrendo TUPLA \/
dias_semana = ('domingo', 'segunda', 'terça',
               'quarta', 'quinta', 'sexta', 'sabado')
for dia in dias_semana:
    print(f'hoje é {dia}')

#percorrendo CONJUNTO \/
for numero in {1,2,3,4,5,6}:
    print(numero, end=' ')