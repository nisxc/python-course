GC_START_YEAR = 1582


def is_equal(days_list, month, days):
    return days_list[month - 1] == days


def days_in_month(isLeap, month, days):
    result_sum = 0
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    equal_check = is_equal(days_in_months, month, days)
    if isLeap:
        if equal_check:
            for d in days_in_months[0:month]:
                result_sum += d

            if month >= 2:
                return result_sum + 1
            else:
                return result_sum
        else:
            for d in days_in_months[0:month - 1]:
                result_sum += d
            return result_sum + days
    else:
        if equal_check:
            for d in days_in_months[0:month]:
                result_sum += d
            return result_sum
        else:
            for d in days_in_months[0:month - 1]:
                result_sum += d
            return result_sum + days


def is_year_leap(year, month, days):

    if year < GC_START_YEAR:
        return print('No within the Gregorial calendar period')
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return days_in_month(True, month, days)
    else:
        return days_in_month(False, month, days)


print(is_year_leap(2001, 2, 22))
test_years = [2000, 2007, 2013]
test_months = [12, 11, 5]
test_days = [31, 12, 6]
test_results = [366, 316, 126]

for i in range(len(test_years)):
    year = test_years[i]
    month = test_months[i]
    day = test_days[i]
    result = is_year_leap(year, month, day)
    if result and result == test_results[i]:
        print('OK')
    else:
        print('Failed')
