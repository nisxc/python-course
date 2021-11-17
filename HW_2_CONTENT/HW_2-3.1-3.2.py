first_numbers = int(input('Enter numbers first number: '))
second_numbers = int(input('Enter numbers second number: '))
third_numbers = int(input('Enter numbers third number: '))
fourth_numbers = int(input('Enter numbers fourth number: '))


if first_numbers > second_numbers and first_numbers > third_numbers and first_numbers > fourth_numbers:
    print('Largest number is:', first_numbers)
elif second_numbers > first_numbers and second_numbers > third_numbers and second_numbers > fourth_numbers:
    print('Largest number is:', second_numbers)
elif third_numbers > second_numbers and third_numbers > first_numbers and third_numbers > fourth_numbers:
    print('Largest number is:', third_numbers)
elif fourth_numbers > second_numbers and fourth_numbers > third_numbers and fourth_numbers > first_numbers:
    print('Largest number is:', fourth_numbers)
else:
    print('Some error right there!')

# print max one in array of numbers
# print(max(first_numbers, second_numbers, third_numbers, fourth_numbers))
