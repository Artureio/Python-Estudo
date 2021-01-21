def fibonacci(qtd):
    resultado = [0,1]

    while len(resultado) < qtd:
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for indice, valor in enumerate(fibonacci(20)):
        print(f'{indice + 1}) {valor }')


