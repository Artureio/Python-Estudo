import csv

with open('contatos.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('nome: {} idade {}'.format(*pessoa))