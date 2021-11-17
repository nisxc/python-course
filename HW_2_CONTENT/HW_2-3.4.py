TAX_PROCENT = 15


def tax_calc(value):
    return round(value + (value * (TAX_PROCENT / 100)), 2)


value_input = float(input('Enter value: '))
print(tax_calc(value_input))
value_input = float(input('Enter value: '))
print(tax_calc(value_input))
value_input = float(input('Enter value: '))
print(tax_calc(value_input))
value_input = float(input('Enter value: '))
print(tax_calc(value_input))
value_input = float(input('Enter value: '))
print(tax_calc(value_input))
value_input = float(input('Enter value: '))
print(tax_calc(value_input))
