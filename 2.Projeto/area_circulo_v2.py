from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('área do Círculo: ',area)
