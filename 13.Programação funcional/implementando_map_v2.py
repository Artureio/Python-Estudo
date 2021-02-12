# mapeando atraves de generator(conceito de lazy evaluation),
# nesse caso, a funcao mapear RETORNA um generator(entre parenteses)
# mapeando item por item utilizando o next()

def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    a = [5, 15, 2]
    resultado = mapear(lambda x: x**2, a)

    print(next(resultado))
    print(next(resultado))
    print(next(resultado))
