def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da funcao: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == "__main__":

    soma(x=2, y=3)
    print('--------------------------')
    sub(10, 2)
