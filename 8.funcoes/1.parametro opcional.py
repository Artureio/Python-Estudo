def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == "__main__":
    #testes (assertions)
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'

    assert tag_bloco('impossível excluir!','error') == \
        '<div class="error">impossível excluir!</div>'
        
    print(tag_bloco('bloco'))