def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError: 
        # 1. Ok!
        # raise
        # 2. Ok! + message
        raise KeyError(f'invalid key {key}')

if __name__ == '__main__':
    
    conn = {
        'host':'localhost',
        'port':3306,
        'service': 'mysql'
    }

    try:
        find_key('host', **conn)
        find_key('ip', **conn)
    except KeyError as e:
        print(f'{e}')
        
    print('---')