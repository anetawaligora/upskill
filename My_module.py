

print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

        return -1

    names = ['arek','ala','ewa','jan']

    i = find_index(names, 'ela')
    print(names[i])

    arek_idx = names.index('ela')
    print(arek_idx)

