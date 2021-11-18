my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
result_list = []
for n in my_list:
    if n not in result_list:
        result_list.append(n)
print(result_list)
