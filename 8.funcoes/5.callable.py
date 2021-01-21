def call(funcao):
    if callable(funcao):
        return funcao()

def bomdia():
    return 'bom dia'

if __name__ == "__main__":
    print(call(bomdia))