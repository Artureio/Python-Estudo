def get_dia_semana(dia):
    dia_semana = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
    if dia in dia_semana:
        return dia_semana.get(dia, 'Dia Invá')


if __name__ == "__main__":

    for dia in range(1, 10):
        if dia in range(2, 7):
            print(f'{dia}) {get_dia_semana(dia)}-feira')

        elif dia == 1 or dia == 7:
            print(f'{dia}) {get_dia_semana(dia)}(FDS)')
