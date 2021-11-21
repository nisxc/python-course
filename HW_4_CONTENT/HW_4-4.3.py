GC_START_YEAR = 1582


def is_year_leap(year, month):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < GC_START_YEAR:
        print('No within the Gregorial calendar period')
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2:
            return days_in_months[month - 1] + 1
        else:
            return days_in_months[month - 1]
    else:
        return days_in_months[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    year = test_years[i]
    month = test_months[i]
    print(year, month, '-->', end=' ')
    result = is_year_leap(year, month)
    if result and result == test_results[i]:
        print('OK')
    else:
        print('Failed')
