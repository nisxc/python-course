hat_list = [1, 2, 3, 4, 5]

userChoose = input('Do you want delete middle element of list?: (y/n) ')

if userChoose.lower() in ['y', 'yes']:
    del hat_list[round((len(hat_list) - 1) / 2)]
    print(hat_list)

del hat_list[len(hat_list) - 1]
print(hat_list)

print(len(hat_list))
