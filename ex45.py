
def get_squares(n):
    return [ v ** 2 for v in range(n + 1)]

# 1. дефиниця на генератора
def gen_squares(n):
    for v in range(n + 1):
        yield v ** 2

if __name__ == '__main__':
    values = get_squares(10)
    print(f'values = {values}')
    # 2. присвояване на променлива
    n_pow = gen_squares(10)

    print(f'type of gen_squares:{type(gen_squares)}')
    print(f'type of n_pow:{type(n_pow)}')
    # 3.1 стойност по стойност
    print(f'1 => {next(n_pow)}')
    print(f'2 => {next(n_pow)}')
    print(f'3 => {next(n_pow)}')
    print(f'4 => {next(n_pow)}')
    print(f'5 => {next(n_pow)}')
    # 3.2 всички наведнъж
    arr = list(n_pow)
    print(f'arr={arr}')

    # 3.3 for
    sqr_5 = gen_squares(5)
    for v in sqr_5:
        print(f'v = {v}')

    sqr_3 = gen_squares(3)
    print(f'1 => {next(sqr_3)}')
    print(f'2 => {next(sqr_3)}')
    print(f'3 => {next(sqr_3)}')
    print(f'4 => {next(sqr_3)}')
    print(f'5 => {next(sqr_3)}')

    print('---')

