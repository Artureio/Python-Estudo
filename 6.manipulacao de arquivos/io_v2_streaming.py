arquivo = open('contatos.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(', ')))

arquivo.close()