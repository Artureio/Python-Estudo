nome, idade = 'Artur', 36

#forma 1 (forma antiga)
    # %s String, %d = inteiro, %f = float, %r = bool
print('Nome: %s Idade: %d' % (nome, idade) )

#forma 2  .format() (python <3.6)
print('nome: {0} Idade: {1}'.format(nome, idade))

#forma 3   f String (interpreta codigos entre chaves)
print(f'nome: {nome} idade: {idade} ex:{2+10}')