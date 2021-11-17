MAGIC_SECRET_NUMBER = 21

number = int(input('Enter integer number: '))

while number != MAGIC_SECRET_NUMBER:
    print("Ha ha! You're stuck in my loop!")
    number = int(input('Enter integer number: '))

print('Well done, muggle! You are free now.')
