
if __name__ == '__main__':
    sqrs = [ x ** 2  for x in range(10)]
    lst = [ (x,y)  for x in range(5) for y in range(5)]

    print(f'values = {sqrs}')
    print(f'lst = {lst}')
    
    txt = 'Lorem ipsum dolor sit amet'

    letters = [ f'[{t}]' for t in txt]
    print(f'letters:{letters}')
    
    print('---')
