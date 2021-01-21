def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


def tag_lista(*itens):
    lista = '\n'.join(f'\t\t<li>{item}</li>' for item in itens)
    return f'\n\t<ul>\n {lista}\n\t</ul>\n'


if __name__ == "__main__":
    print(tag_bloco('versao 1'))
    print(tag_bloco('versao 2', 'info', True))
    print(tag_bloco(inline=True, texto='versao 2 com ordem nao-padrao', classe='info'))
    print(tag_bloco(tag_lista('Versao 3','Funcao dentro de funcao', 'Teste'), classe='warning',inline=False))
