def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    print(tag_bloco('versao 1'))
    print(tag_bloco('versao 2', 'info', True))
    print(tag_bloco(inline=True, texto = 'versao 2 com ordem nao-padrão', classe='info'))
