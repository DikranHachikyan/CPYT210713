
def sum_numbers(n):
    print(f'n = {n}')

    if n > 0:
        return n + sum_numbers(n - 1)
    return 0

if __name__ == '__main__':
    
    x = sum_numbers(5)
    print(f'x={x}')
    print('---')

