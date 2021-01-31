from app import Cliente
from app import Compra
from app import Vendedor


def main():
    c1 = Compra()
    c1.registrar_compra('Miojo')
    c1.total_compras()
    print
if __name__ == '__main__':
