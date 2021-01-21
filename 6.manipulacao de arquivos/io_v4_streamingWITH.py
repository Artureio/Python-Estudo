#o bloco WITH fecha o arquivo automaticamente no final

with open('contatos.csv') as arquivo:
    for registro in arquivo:
        print('nome: {} idade {}'.format(*registro.strip().split(', ')))

if arquivo.closed:
    print('arquivo fechado')