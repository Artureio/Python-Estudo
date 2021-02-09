def multiplicar(x):
    def calcular(y):
        return x*y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)

    print(f'O triplo de 3:  {triplo(3)}')
    print(f'o dobro de 3: {dobro(3)}')
