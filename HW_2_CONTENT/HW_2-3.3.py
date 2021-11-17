CORRECT_PLANT_NAME = 'Spathiphyllum'

writtenName = input('Enter plant name: ')

if writtenName[0].isupper() and writtenName.lower() == CORRECT_PLANT_NAME.lower():
    print('Yes - Spathiphyllum is the best plant ever!')
elif writtenName[0].islower() and writtenName.lower() == CORRECT_PLANT_NAME.lower():
    print('No, I want a big Spathiphyllum!')
else:
    print('Spathiphyllum! Not', writtenName)
