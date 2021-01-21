# packing (recebe varios argumentos e transforma em uma tupla.)
# na declaração da função, o argumento precisa ter um asterisco
# para indicar que receberá 'n' argumentos e depois transformálo na tupla.
def packing_soma(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

#unpacking: define uma quantidade certa de parametros;
#depois, usa uma tupla (ou lista) com a quantidade a mesma qtd de parametros
#para fazer o enpacotamento da tupla dentro dos parametros
def unpacking_soma(a, b, c):
    return a+b+c


if __name__ == "__main__":

    print(packing_soma(1, 6, 8, 3, 4, 6))  # packing

    a = (20,30,22)
    print(unpacking_soma(*a)) #unpacking (observe o asterisco)