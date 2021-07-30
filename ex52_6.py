from time import time, sleep 
from functools import wraps

def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

def to_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}' for v in args]
        return func(*args, **kwargs)
    return wrapper

@to_string
def concat(*args, **kwargs):
    '''Concatenate list elements with sep'''
    sep = kwargs.get('sep', ';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna', 'maria', 'markus','jane']
    values = [1,2,3,4,5]

    print(concat(*users, sep = ' # '))
    print(concat(*values, sep = '|'))

    print(concat.__original(*users, sep = '/'))
    # print(concat.__original(*values, sep = 'x'))
    concat = concat.__original
    print(concat(*users, sep = '->'))
    # print(concat(*values, sep = 'x'))

    print = to_uppercase(print)
    print('hello python', 'lorem ipsum')
    print(1,2,'a',4,5)

    print = print.__original

    print('hello python', 'lorem ipsum')
    print('---')