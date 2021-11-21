GC_START_YEAR = 1582


def is_year_leap(year):
    if year < GC_START_YEAR:
        print('No within the Gregorial calendar period')
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    year = test_data[i]
    print(year, '-->', end=' ')
    result = is_year_leap(year)
    if result and result == test_results[i]:
        print('OK')
    else:
        print('Failed')
