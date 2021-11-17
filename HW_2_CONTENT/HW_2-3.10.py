VOWELS = ['A', 'E', 'I', 'O', 'U']

word = input('Enter word: ').upper()
result = ''
for w in word:
    if w not in VOWELS:
        result += w
print(result)
