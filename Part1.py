import copy

def convert(some_list):
     ###copy list to a new List
    new_list=copy.deepcopy(some_list)
    ###insert 'and' into the new List
    new_list.insert(-1, 'and')
    new_string = ''

    for i, x in enumerate(new_list):
        if i < new_list.index('and'):
            new_string = new_string + x +', '
        elif i == new_list.index('and'):
            new_string = new_string + x + ' '
        else:
            new_string = new_string + x + '.'

    ###return valuye
    return new_string


###call convert to convert list to string
some_list=['carrot', 'lettuce', 'onion', 'radish']

print(convert(some_list))
