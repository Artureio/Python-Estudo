# Listar toda a tabuada de multiplicação de 1 a 9
# usando list comprehension, em apenas uma linha.
# Não é válido utilizar linha de código separadas 
# com : (dois pontos).

print('\n'.join (f'{x} x {y} = {x*y}' for x in range(1, 10) for y in range(1, 10)))

