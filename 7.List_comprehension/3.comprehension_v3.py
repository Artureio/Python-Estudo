generator = (i ** 2 for i in range(10) if i %2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

#com FOR

generator2 = (i ** 3 for i in range(10))
for numero in generator2:
    print(numero)