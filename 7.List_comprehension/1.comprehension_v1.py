#sintaxe normal
dobros = []

for i in range(1,11):
    dobros.append(i*2)
print(dobros)

#Comprehension

dobros2 = [i*2 for i in range(10)]
print(dobros2)

# #sequencia fibonnaci normal
# fibo = [0,1]
# for i in range(10):
#     fibo.append(sum(fibo[-2:]))
# print(fibo)

# #sequencia fibonacci COMPREHENSION
# fibo2 = [0,1 for i in range(10):sum([-2:])]
