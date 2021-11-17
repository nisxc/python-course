GC_START_YEAR = 1582

yearInput = int(input('Enter year: '))

if yearInput < GC_START_YEAR:
    print('No within the Gregorial calendar period')
elif yearInput % 4 == 0 and yearInput % 100 != 0 or yearInput % 400 == 0:
    print('Leap year')
else:
    print('Common year')
