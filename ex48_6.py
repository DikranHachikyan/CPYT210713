from time import time, sleep 
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(f'doc str:{func.__doc__}')
        print(f'{func.__name__}: {time() - t:.4f}')
    return wrapper


@measure
def foo(sleep_time = 0.3):
    '''Function foo sleeps sleep_time seconds'''
    # print(f'before sleep')
    sleep(sleep_time)
    # print(f'after sleep')


if __name__ == '__main__':
    
    
    foo()
    foo(0.5)
    print(f'{foo.__name__} doc str:{foo.__doc__}')
    print('---')