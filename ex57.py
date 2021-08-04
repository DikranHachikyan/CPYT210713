

if __name__ == '__main__':
    
    actions = {
        '+': lambda a,b: a + b
    }

    while True:
        try:
            op = input('action (+, q-quit):')
            if op == 'q': quit()
            
            val1 = float(input('first number:'))
            val2 = float(input('second number:'))

            result = actions[op](val1,val2)

        except (ValueError, KeyError) as e:
            print(f'Invalid number or action ({e})')
        except Exception as e:
            print(f'Unknown error ({e})')
        else:
            print(f'{val1} {op} {val2} = {result}')
            print('--- else ---')
            continue
        finally:
            print('---finally---')



    print('---')