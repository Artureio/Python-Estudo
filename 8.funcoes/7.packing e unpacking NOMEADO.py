# **kwargs

def packing_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao}: {piloto}')


def unpacking_f1(primeiro, segundo, terceiro):
    print(f'1: {primeiro}')
    print(f'2: {segundo}')
    print(f'3: {terceiro}')

        



if __name__ == "__main__":
    packing_f1(primeiro ='Hamilton',
               segundo='Tesla',
               terceiro='Schumacker')

    unpacking = {'terceiro':'pedro',
                 'primeiro':'joao',
                 'segundo':'thiago'}

    unpacking_f1(**unpacking)