def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=', ')

    while ultimo < limite:
        # substituindo valores das variaveis usando PACKING
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=', ')


if __name__ == '__main__':
    fibonacci(20000)
