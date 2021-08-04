class ParamNotFoundError(Exception):
    pass

def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError: 
        raise ParamNotFoundError(f'parameter {key} not found!')

if __name__ == '__main__':
    
    conn = {
        'host':'localhost',
        'port':3306,
        'service': 'mysql'
    }

    try:
        find_key('host', **conn)
        find_key('ip', **conn)
    except ParamNotFoundError as e:
        print(f'{e}')
        
    print('---')