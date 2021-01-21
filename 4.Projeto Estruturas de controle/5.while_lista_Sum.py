def fibonacci(limite):
    resultado = [0,1]

    while resultado[-1] <= limite:
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for fib in fibonacci(20000):
        print(fib)
