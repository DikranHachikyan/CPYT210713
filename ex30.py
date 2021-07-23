# глобална променлива
port = 3306

# 1. дефиниция на функцията
def sum_numbers(a, b, d = None):
    # c - локална променлива
    c = a + b + d if d else a + b
    return c


if __name__ == '__main__':
    # 2. извикване на функцията

    x,y = 10,12
    r1 = sum_numbers(x,y)
    print(f'{x} + {y} = {r1}')

    z = 33
    r1 = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {r1}')
    
    print('---')
