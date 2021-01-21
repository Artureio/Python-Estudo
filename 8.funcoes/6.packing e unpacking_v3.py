def tag_bloco(conteudo,*args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = '\n'.join(f'\t\t<li>{item}</li>' for item in itens)
    return f'\n\t<ul>\n {lista}\n\t</ul>\n'


if __name__ == "__main__":
    print(tag_bloco(tag_lista('item ', 'item2'),
                    classe='warning', inline=True))
    print(tag_bloco(tag_lista,'item', 'item2',
                    classe='warning', inline=True))

