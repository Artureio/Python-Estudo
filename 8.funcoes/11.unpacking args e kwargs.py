
block_attributes = ('accesskey',)
li_attributes = ('type',)


def filtered_attrs(kwargs, filter):
    return ' '.join(f'{k}="{v}"' for k, v in kwargs.items() if k in filter)


def build_block(conteudo, *args, classe='success', inline=False, **kwargs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = {'class': classe}
    atributos.update(kwargs)
    return f'< {tag} {filtered_attrs(atributos, block_attributes + ("class",))}\
     > {html} < /{tag} >'


def build_list(*itens, **kwargs):
    lista = ''.join(
        f'<li {filtered_attrs(kwargs, li_attributes)} \
        >{item}</li>'for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(build_block('bloco'))
    print(build_block('linha', inline=True))
    print(build_block('falhou', classe='error'))
    print(build_block(build_list('Sabado', 'Domingo'), classe='info'))
    print(build_block(build_list, 'Sabado', 'Domingo', classe='info'))
    print(build_block(build_list, 'Sabado', 'Domingo',
                      classe='info', accesskey='m', type='square'))
