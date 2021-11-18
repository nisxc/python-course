result_list = []
s = input('Enter numbers by space ')
li1 = s.split()
li1.sort()
index = 0
for n in range(len(li1) - 1):
    index = n
    if li1[index] not in result_list and li1[index] == li1[index + 1]:
        result_list.append(li1[index])
print(result_list)
