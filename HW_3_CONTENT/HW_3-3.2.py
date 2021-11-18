STEP_3_PEOPLE = ['Stu Sutcliffe', 'Pete Best']

beatles = []
print('Step 1:', beatles)

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print('Step 2:', beatles)

for p in STEP_3_PEOPLE:
    userInput = input('Do you want to add ' + p + ': (y/n) ',)
    beatles.append(p)
print('Step 3:', beatles)

temp = []
for ep in beatles:
    if ep not in STEP_3_PEOPLE:
        temp.append(ep)

beatles = temp
print('Step 4:', beatles)

beatles.insert(0, 'Ringo Starr')
print('Step 5:', beatles)
