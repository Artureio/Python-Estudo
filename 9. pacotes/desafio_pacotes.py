from app.negocio import check_exists
from app.negocio.backend import add_nome as add
from app.utils.generators import nome_proprio


def main():
    while True:
        nome = nome_proprio()
        if not check_exists(nome):
            add(nome)
            break
    print(f'Criado novo nome de testes: "{nome}"')


main()
