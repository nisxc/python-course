s = input('Enter number range by space (start,end) ')
li1 = s.split(',')
numbers = []
sum = 0
for n in range(int(li1[0]), int(li1[1]) + 1):
    if n % 3 == 0:
        sum += n
        numbers.append(n)

print(sum / len(numbers))
