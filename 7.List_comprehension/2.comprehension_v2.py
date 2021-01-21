# sintaxe normal
dobro_dos_pares = []

for i in range(1, 11):
    if(i % 2 == 0):
        dobro_dos_pares.append(i*2)
print(dobro_dos_pares)

# Comprehension

dobro_dos_pares2 = [i*2 for i in range(1, 11) if i % 2 == 0]
print(dobro_dos_pares2)
