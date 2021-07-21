
if __name__ == '__main__':
    app_config = {
        'title':'Text Editor',
        'version':'1.2.3',
        'n_proc':10,
        'max_memory':4096,
        'margins':[5,10,5,10]
    }

    for item in app_config.items():
        key, value = item
        print(f'key = {key} => {value}')

    print('---')
