def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de Idade'
    elif idade in range (18,64):
        return 'adulto'
    elif idade in range (65, 99):
        return 'Idoso'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'


if __name__ == "__main__":
    idades = (1,2,35,36,200,100,99,60,65,-1)
    for idade in idades:
        print(f'{idade}: {faixa_etaria(idade)}')
