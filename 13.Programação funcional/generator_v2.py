from random import randint


def gen():
    a = 0
    while True:
        a = randint(0,10)
        yield f'Valor gerado: {a}'


if __name__ == '__main__':
    print(next(gen()))
    print(next(gen()))
    print(next(gen()))
    print(next(gen()))
    print(next(gen()))
    print(next(gen()))
    print(next(gen()))