# глобална променлива
port = 3306

def show(title, a = 100, *args, kw1, kw2='A', **kwargs):
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

    print('keyword-only args')
    print(f'kw1={kw1}, kw2={kw2}')

if __name__ == '__main__':

    
    # 4
    app = {
        'port':3300,
        'version':'1.4',
        'db':'northwind'
    }

    show('Text Editor', 3, 10, 20, 30, 40, kw1=-10, kw2='Z', **app)
    print('---')

