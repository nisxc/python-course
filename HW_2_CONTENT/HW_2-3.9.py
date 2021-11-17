VOWELS = ['A', 'E', 'I', 'O', 'U']

word = input('Enter word: ').upper()

for w in word:
    if w not in VOWELS:
        print(w)
