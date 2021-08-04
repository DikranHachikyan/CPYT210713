def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError as e:
        # 1. bad idea
        # pass
        # 2. ??
        # print(f'invalid key {key} ({e})')
        # 3. Ok! 
        raise

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
        print(f'invalid key:{e}')
        
    print('---')