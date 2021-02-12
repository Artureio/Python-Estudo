# utilizando paradigma funcional, crie uma função que resolva o MDC

# 1-dividir o número maior pelo número menor
# 2-dividir o ultimo divisor pelo resto da divisão anterior, e assim em diante
# 3-quando o resto for zero, achou o divisor comum


def mdc(lista):
    resto = max(lista) % min(lista)
    ultimodivisor = min(lista)

    while resto == True:
        divisor = ultimodivisor / resto
        resto = ultimodivisor % resto

    return ultimodivisor if resto == False else resto


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
