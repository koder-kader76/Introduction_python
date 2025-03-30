# 3. Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

# first = input("Enter the first number: ")
# second = input("Enter the second number: ")
# print(f"{first} * {second} = "       
#       f"{float(first) * float(second)}")

#LS Solution

def mulitply(left, right):
    return left * right

def get_number(prompt):
    number = float(input(prompt))
    return number

first = get_number("Enter the first number: ")
second = get_number("Enter the second number: ")
product = mulitply(first, second)
print(f"{first} * {second} = {product}")