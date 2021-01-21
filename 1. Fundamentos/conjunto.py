a={1,2,3,6}
b={3,4,5,6}
c={6,7,8,9,10}
d = a - b - c


uniao = a.union(b,c)
intersecao = a.intersection(b) 

#'<=' = subconjunto
print(c <= uniao)

#'>=' = superconjunto
print(uniao >= b)

print(uniao - {3})
print(uniao )



if 3 in a and 3 in b and 3 in c:
    print('ta nas 3')
else:
    print('nao ta nas 3')

#mesma coisa do codigo acima
if 3 in a.intersection(b,c):
    print('ta nas 3')
else:
    print('nao ta nas 3')