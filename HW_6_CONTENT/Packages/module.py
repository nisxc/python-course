__counter = 0


def sum(list):
    global __counter
    __counter += 1
    sum = 0
    for e in list:
        sum += e
    return sum


def prod(list):
    global __counter
    __counter += 1
    prod = 1
    for e in list:
        prod *= e
    return prod


if __name__ == '__main__':
    print('I prefer to be a module, but I can do some tests for you.')
    list = [i+1 for i in range(5)]
