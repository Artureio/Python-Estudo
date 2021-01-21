def fibo(qtd, sequencia=(0,1)):
    
    if len(sequencia) == qtd:
        return sequencia
    return fibo(qtd, sequencia + (sum(sequencia[-2:]),))


for fib in fibo(20):  
    print(fib)
