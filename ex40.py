
# def f():
#     def g():
#         def h():
#             pass

def sort_priority(values, group):
    found = False

    def sort_helper(el):
        if el in group:
            nonlocal found
            found = True
            return (0,el)
        
        return (1,el)

    values.sort(key = sort_helper)
    return found



if __name__ == '__main__':
    numbers = [10, 8, 4, 1, 3, 5, 7, 6]

    grp = {4, 5, 6}

    print(f'before numbers:{numbers}')
    is_found = sort_priority(numbers, grp)
    print(f'after is found:{is_found} numbers:{numbers}')

   
    print('---')

