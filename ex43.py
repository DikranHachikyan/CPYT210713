
def foo(c = None, b = None):
    if not c: c = []
    if not b: b = {}
    
    print(f'c = {c}')
    print(f'b = {b}')
    print(' - ' * 20)
    n = len(c)
    c.append(n)
    b[n] = n


if __name__ == '__main__':
    foo()    
    foo([3,8,1], {'z':100})    
    foo()
    foo([31,18,11], {'x':100})    
    foo()
    print('---')

