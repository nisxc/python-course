def fib(n):
    try:
        fib_list = [1, 1]
        for i in range(1, n + 1):
            if len(fib_list) != n:
                fib_list.append(fib_list[i] + fib_list[i - 1])
            else:
                break
        return fib_list
    except:
        print('Sorry, something going wrong!')


def fib_sum(list):
    sum = 0
    for n in list:
        sum += n
    return sum


print('Fibonacci:', fib(10))
print('Fibonacci sum', fib_sum(fib(10)))
