# глобална променлива
port = 3306

def show(title, a = 100, *args, **kwargs):
    print(f'title = {title}')

    print('Optional Params:')
    print(f'a = {a}')

    print('args:')
    for v in args:
        print(v, end=' ')
    print()

    print(f'kwargs:{kwargs}')
    kw_params = {
        'version': kwargs.get('version', '1.0'),
        'path': kwargs.get('path','/tmp')
    }
    print(f'kw_params:{kw_params}')

if __name__ == '__main__':
    # 1
    show('Text Editor')

    # 2
    show('Text Editor', 3)

    # 3
    show('Text Editor', 3, 10, 20, 30, 40)
    
    # 4
    app = {
        'port':3300,
        'version':'1.4',
        'db':'northwind'
    }

    show('Text Editor', 3, 10, 20, 30, 40, **app)
    print('---')

