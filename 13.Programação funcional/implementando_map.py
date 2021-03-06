# mapeando atraves de generator(conceito de lazy evaluation),
# mapeando item por item utilizando o next()

def mapear(funcao, lista):
    

    for elemento in lista:
        yield funcao(elemento)


if __name__ == '__main__':
    a = [5, 15, 2]
    resultado = mapear(lambda x: x**2, a)

    print(next(resultado))
    print(next(resultado))
    print(next(resultado))
