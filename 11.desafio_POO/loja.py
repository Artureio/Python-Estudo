from datetime import datetime
from app import Cliente, Vendedor, Compra


def main():
    artur = Cliente('artur henrique', 44)
    theo = Vendedor('theo henrique', 36, 1000)

    compra1 = Compra(theo, datetime.now(), 512)
    compra2 = Compra(theo, datetime(2018, 6, 4), 256)

    artur.registrar_compra(compra1)
    artur.registrar_compra(compra2)
    
    print(f'Cliente: {artur}', '(adulto)' if artur.isAdult() else '')
    print(f'Vendedor: {theo}')
    print(f'Total: {artur.total_compras()} em {len(artur.compras)} compras')
    print(f'ultima compra: {artur.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
