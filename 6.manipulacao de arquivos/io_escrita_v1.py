with open('contatos.csv') as arquivo:
    with open('contatos.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(', ')
            print('nome: {} idade {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('escrita finalizada',)
        

    