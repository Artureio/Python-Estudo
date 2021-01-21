dicionario = {i: i * 2  for i in range(10)}

print(dicionario)

tabuada = {i: i for i in range(10)}

for chave, valor in tabuada.items():
    print(f'Tabuada do {chave}:')
     
    for chave1, valor1 in tabuada.items():
        print(f'{valor} x {valor1} ={valor * valor1}')
