s = input('Enter numbers by space ')
li1 = s.split()
numbers = []
sum = 0
for w in li1:
    target = int(w)
    numbers.append(target)
    sum += target

print(sum / len(numbers))
