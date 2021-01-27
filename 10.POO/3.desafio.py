class Carro:
    def __init__(self, velAtual=0, velMax=200):
        self.velAtual = velAtual
        self.velMax = velMax
        print(
            f'Objeto: {self} \nVelocidade Inicial: {velAtual}'
            '\nVelocidade Maxima: {velMax}')

    def acelerar(self, qtd):
        print(f'velocidade atual: {self.velAtual}')

        for qtd in range(qtd):
            self.velAtual = self.velAtual + 8

            if self.velAtual >= self.velMax:
                print('velocidade maxima excedida')
                break

        print(
            f'velocidade apos acelerar: {self.velAtual}'
            '\n..........................')

    def freiar(self, qtd):
        print(f'velocidade atual: {self.velAtual}')

        for qtd in range(qtd):
            self.velAtual = self.velAtual - 25

            if self.velAtual <= 0:
                print('velocidade chegou a ZERO')
                self.velAtual = 0
                break

        print(
            f'velocidade apos freiar: {self.velAtual}'
            '\n..........................')


if __name__ == '__main__':
    c1 = Carro()
    c1.acelerar(10)
    c1.acelerar(10)
    c1.acelerar(10)
    c1.freiar(5)
    c1.freiar(3)
    c1.freiar(3)
