def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=', ')

    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=', ')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(20000)
