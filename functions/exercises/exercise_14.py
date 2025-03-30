# 14. Identify all of the identifiers on each line of the following code.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# line 3: mulitply, left, right
# line 4: left, right
# line 6: get_num, prompt
# line 7: float, input, prompt
# line 9: first_number, get_num
# line 10: second_number, get_num
# line 11: product, multiply, first_number, second_number
# line 12: print, first_number, second_number, product