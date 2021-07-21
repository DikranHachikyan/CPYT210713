
if __name__ == '__main__':
    app_config = {
        'title':'Text Editor',
        'version':'1.2.3',
        'n_proc':10,
        'max_memory':4096,
        'margins':[5,10,5,10]
    }

    for key in app_config:
        print(f'key = {key} => {app_config[key]}')
        
    print('---')
