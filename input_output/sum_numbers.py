# Add Two Numbers

# Let's write a program that asks for two numbers from the user, adds them, and then displays the result. 

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = int(number1) + int(number2)

print(f"The numbers {number1} and {number2} "
      f"add to {sum}")

# first output - but numbers concatenated as strings
# Enter the first number: 12
# Enter the second number: 23
# The numbers 12 and 23 add to 1223


# second output - numbers coerced into integers before adding
# Enter the first number: 12
# Enter the second number: 23
# The numbers 12

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)

print(f"The numbers {number1} and {number2} "
      f"add to {sum}")

# third output - coercing numbers into floats
# Enter the first number: 12
# Enter the second number: 35
# The numbers 12 and 35 add to 47.0