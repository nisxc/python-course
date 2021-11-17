SECRET_EXIT_WORD = 'chupacabra'

word = input('Enter word: ')

isWorking = True

while isWorking:
    if word == SECRET_EXIT_WORD:
        isWorking = False
        # break
    else:
        word = input('Enter word: ')
