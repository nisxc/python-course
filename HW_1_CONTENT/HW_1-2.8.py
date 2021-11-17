VALID_OPERATORS = ['+', '-', '/', '*', '**', '//', '%']

userX = input('Enter x value: ')
userY = input('Enter y value: ')
userOperator = input('Enter operator: ')

if userOperator in VALID_OPERATORS and userX and userY:
    if userOperator == '+':
        print(int(userX + userY))
    elif userOperator == '-':
        print(int(userX - userY))
    elif userOperator == '/':
        print(int(userX / userY))
    elif userOperator == '*':
        print(int(userX * userY))
    elif userOperator == '**':
        print(int(userX ** userY))
    elif userOperator == '//':
        print(int(userX // userY))
    elif userOperator == '%':
        print(int(userX % userY))
else:
    print('Sorry, unsupported operator or you miss value enter!')
