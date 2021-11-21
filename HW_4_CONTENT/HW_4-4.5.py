userInput = int(input('Enter number: '))
n = 1
result = False
while n < userInput:
    if n % 2 == 0:
        print('This number is not primal:', n)
        result = False
    else:
        print('This number is primal:', n)
        result = True
    n += 1
print('Result if this number is primal:', result)
