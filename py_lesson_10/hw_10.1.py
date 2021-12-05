def cr_counter(fileName):
    chars = {chr(ch): 0 for ch in range(ord('a'), ord('z') - 1)}
    for row in open(fileName, 'rt'):
        for ch in row:
            if ch in chars:
                chars[ch] += 1
    for i in chars:
        if chars[i]:
            print(i, ':', chars[i])


file = input('Enter file name: ')
try:
    cr_counter(file)
except:
    print('F')
