def letras():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'
    yield 'f'
    yield 'g'
    yield 'h'
    yield 'i'
    yield 'j'

if __name__ == '__main__':
    gerador = letras()
    print(type(gerador))

    while True:
        print(next(gerador))
