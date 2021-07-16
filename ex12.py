def new_file():
    return 'Create new file'

def open_file():
    return 'Open file ...'

def save_file():
    return 'Save file'

def quit_app():
    print('Quit Editor')
    quit()


actions = {
    'n':new_file,
    'p':open_file,
    's':save_file,
    'q':quit_app
}

ch = input('Command (n-new, p-open, s-save,q-quit):')

if ch in actions:
    result = actions[ch]()
    print(f'action:{result}')
else:
    print(f'Unknown command:{ch}')

print('---')
