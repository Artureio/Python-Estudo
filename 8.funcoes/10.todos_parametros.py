def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs:{kwargs}')

if __name__ == "__main__":
    todos_params(1,2,3,4,teste='testando', show = True)
     