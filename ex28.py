# глобална променлива
port = 3306

# 1. дефиниция на функцията
def sum_numbers(a, b):
    # c - локална променлива
    c = a + b
    return c


if __name__ == '__main__':
    # 2. извикване на функцията

    r1 = sum_numbers(5,6)
    print(f'result = {r1}')

    x,y = 10,12
    r1 = sum_numbers(x,y)
    print(f'{x} + {y} = {r1}')
    
    print('---')
