def arrrowPrint(size):
    print(' ' * 4, end='*\n')
    print(' ' * 3, '*', ' ' * 2, end='*\n', sep='')
    print(' ' * 2, '*', ' ' * 4, end='*\n', sep='')
    print(' ', '*', ' ' * 6, end='*\n', sep='')
    print('*' * 3, ' ' * 3, end='***\n')
    print(' ' * 1, '*', ' ' * 3, end='*\n')
    print(' ' * 1, '*', ' ' * 3, end='*\n')
    print(' ' * 1, '*' * 6)


userInput = input('Print arrow: ')
if userInput and userInput not in ['no', 'hate you', 'quit', 'exit']:
    arrrowPrint(userInput)
else:
    print('''
    |-------------------------|
    |Sorry, see you next time!|
    |-------------------------|
    ''')
