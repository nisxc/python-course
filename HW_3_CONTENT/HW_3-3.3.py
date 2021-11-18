# basic_list = [10, 2, 11, 3, 5] initial list
SORT_TYPES = ['increased', 'reversed']
swapped = True

user_array = input('Enter number that you want to sort: ')
type = input('Select type of sort: (increased/reversed) ')

n_array = user_array.split(',')

if type not in SORT_TYPES:
    print('Sorry but you choose wrong sort type! Try again next time')
else:
    while swapped:
        swapped = False
        for i in range(len(n_array) - 1):
            if int(n_array[i]) > int(n_array[i + 1]):
                swapped = True
                n_array[i], n_array[i + 1] \
                    = n_array[i + 1], n_array[i]
if type == SORT_TYPES[0]:
    print('Result of normal sort:', n_array)
else:
    n_array.reverse()
    print('Result of reversed sort:', n_array)
