# listar todos os meses com 31 dias (MEU JEITO)
from locale import LC_ALL, setlocale
from calendar import mdays, month_name

setlocale(LC_ALL, 'pt_BR')


juntar_meses = zip(month_name, mdays)

a_dictionary = dict(juntar_meses)

trinta_e_um = filter(lambda i: i[1] == 31, a_dictionary.items())

print(tuple(trinta_e_um))
