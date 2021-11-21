CHOSES = ['Yes', 'y', 'yes', 'start']
OPERATIONS = ["Addition", "Subtraction",
              "Multiplication", "Division", "Modulus", "Exponentiation", "Floor division"]


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if not b:
        print('Wrong value')
    return a / b


def mod(a, b):
    return a % b


def exp(a, b):
    return a ** b


def fd(a, b):
    return a // b


def calculator():
    while True:
        userChoose = input('Are you want to start calculator?: (y/n) ')
        if userChoose not in CHOSES:
            break
        print("Please select operation\n"
              "1. Addition\n"
              "2. Subtraction\n"
              "3. Multiplication\n"
              "4. Division\n"
              "5. Modulus\n"
              "6. Exponentiation\n"
              "7. Floor division\n")
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))
        operation = input('Enter operation: ')

        if first and second and operation:
            if operation == "Addition":
                print(add(first, second))
            elif operation == "Subtraction":
                print(sub(first, second))
            elif operation == "Multiplication":
                print(mult(first, second))
            elif operation == "Division":
                print(div(first, second))
            elif operation == "Modulus":
                print(mod(first, second))
            elif operation == "Exponentiation":
                print(exp(first, second))
            elif operation == "Floor division":
                print(fd(first, second))
            else:
                print('Something goes wrong, try it again')
        else:
            continue


calculator()
print('Calculator execution was ended!')
