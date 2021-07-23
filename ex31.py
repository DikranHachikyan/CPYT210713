# глобална променлива
port = 3306

# 1. дефиниция на функцията
def sum_numbers(a, b, *args):
    # c - локална променлива
    print(f'args:{type(args)} value:{args}')
    c = a + b
    for v in args:
        c += v
    
    return c


if __name__ == '__main__':
    # 2. извикване на функцията

    x,y = 10,12
    r1 = sum_numbers(x,y)
    print(f'{x} + {y} = {r1}')

    z = 33
    r1 = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {r1}')
    
    m, n, s = 2, 5, 6
    r1 = sum_numbers(x, y, z, m, n, s)
    print(f'{x} + {y} + {z} + {m} + {n} + {s} = {r1}')

    values = [i for i in range(20,30)]

    r1 = sum_numbers(x, y, *values)
    print(f'{x} + {y} + ' + ' + '.join(map(str,values)) + f' = {r1}' )
    print('---')
