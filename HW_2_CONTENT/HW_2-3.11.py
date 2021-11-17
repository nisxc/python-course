steps = 0
c0 = int(input('Enter number: '))


while c0 > 0 and c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
        steps += 1
        print(c0)
    else:
        c0 = 3 * c0 + 1
        steps += 1
        print(c0)
    print('Steps was made:', steps)
