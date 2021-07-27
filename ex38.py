# глобална променлива
port = 3306

def show(title, *, b = 100):
    print(f'title  = {title}, b = {b}')

if __name__ == '__main__':

    show('Text Editor')

    show('Text Editor', b = 2)

    show('Text Editor', b = 12)

    print('---')

