userX = int(input('Enter x value: '))

if userX:
    y = 1 / userX + (1 / userX + (1 / userX + (1/userX)))
    print(y)
else:
    print('Sorry, you write unsupported x value!')
