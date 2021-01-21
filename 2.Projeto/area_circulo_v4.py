from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    SUCCESS = '\033[92m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {sys.argv[0][43:]} + <raio>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        print(TerminalColor.ERRO,
              'O Raio deve ser um valor numérico positivo!',
              TerminalColor.NORMAL)
        help()
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print(TerminalColor.SUCCESS, 'área do Círculo: ',
          area, TerminalColor.NORMAL)
