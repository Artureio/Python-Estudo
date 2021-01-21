try:
    arquivo = open('contatos.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(', ')))
finally:
    arquivo.close()

if arquivo.closed:
    print('arquivo já foi fechado')