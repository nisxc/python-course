def factorial(n):
    result = 1
    try:
        for i in range(n + 1):
            if i >= 1:
                result *= i
        return result
    except:
        print('Sorry, something go wrong!')


print(factorial(7))
