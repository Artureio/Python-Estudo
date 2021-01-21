import csv

def read(arquivo):
    with open(arquivo, encoding='UTF-8') as entrada:
        for cidade in csv.reader(entrada):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    import sys
    read(sys.argv[1])
