def funcao(nota):
    if nota >= 0 and nota <= 1:
        conceito = 'E-'
    elif nota >= 1.1 and nota <= 2:
        conceito = 'E'
    elif nota >= 2.1 and nota <= 3:
        conceito = 'D-'
    elif nota >= 3.1 and nota <= 4:
        conceito = 'D'
    elif nota >= 4.1 and nota <= 5:
        conceito = 'C-'
    elif nota >= 5.1 and nota <= 6:
        conceito = 'C'
    elif nota >= 6.1 and nota <= 7:
        conceito = 'B-'
    elif nota >= 7.1 and nota <= 8:
        conceito = 'B'
    elif nota >= 8.1 and nota <= 9:
        conceito = 'A-'
    elif nota >= 9.1 and nota <= 10:
        conceito = 'A'
    else:
        conceito = 'Nota inválida'
    return print(f'Sua nota é: {conceito}!')


if __name__ == "__main__":
    nota = float(input('Informe a nota: '))

    funcao(nota)
