MILES_TO_KILOMETERS = 1.61
VALID_ANSWER = ['miles', 'mile', 'kilometer', 'kilometers']

lenthUnit = input('Enter length unit: ')

if lenthUnit and lenthUnit in VALID_ANSWER:
    unitCount = input('Enter ' + str(lenthUnit) + ' count: ')
    if lenthUnit in VALID_ANSWER[0:2]:
        print(str(round(int(unitCount) / MILES_TO_KILOMETERS, 4)) + ' kilometres')
    else:
        print(str(round(int(unitCount) * MILES_TO_KILOMETERS, 4)) + ' miles')
else:
    print('Sorry, wrong unit!')
