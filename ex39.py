# глобална променлива
port = 3306

def show():
    global port
    
    port = 22
    print(f'show port = {port}')

if __name__ == '__main__':

    print(f'before port = {port}')
    show()
    print(f'after port = {port}')
    print('---')

