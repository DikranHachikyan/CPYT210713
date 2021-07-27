
def foo(c):
    c = 10
    print(f'c = 10')


def show(values):
    values.sort()
    print(f'values:{values}')




if __name__ == '__main__':
    numbers = [10, 8, 4, 1, 3, 5, 7, 6]
    x = 12

    foo(x)
    print(f'after x={x}')
    
    show(numbers)
    print(f'after numbers:{numbers}')
    print('---')

