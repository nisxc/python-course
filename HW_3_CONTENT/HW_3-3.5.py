numbers = []
sum = 0
s = input('Enter numbers by space ')
li1 = s.split()
for w in li1:
    target = int(w)
    numbers.append(target)
    sum += target
print(numbers)
print(sum)
