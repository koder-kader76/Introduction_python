# 7. Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive) 
# the value is between 51 and 100 (inclusive) 
# the value is greater than 100
# the value is less than 0

# write a function that takes a single integer argument
def number_range(num):
    # the value is between 0 and 50 (inclusive) 
    # the value is between 51 and 100 (inclusive) 
    # the value is greater than 100
    # the value is less than 0
    if num > 100:
        print(f'the {num} is greater than 100')
    elif num >= 51:
        print(f'the {num} is between 51 and 100')
    elif num >= 0:
        print(f'the {num} is between 0 and 50')
    else:
        print(f'the {num} is less than 0')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
    

def number_range2(num2):
    # the value is between 0 and 50 (inclusive) 
    # the value is between 51 and 100 (inclusive) 
    # the value is greater than 100
    # the value is less than 0
    if num2 < 0:
        print(f'the {num2} is less than 0')
    elif num2 < 51:
        print(f'the {num2} is between 0 and 50')
    elif num2 < 101:
        print(f'the {num2} is between 51 and 100')
    else:
        print(f'the {num2} is greater than 100')

number_range2(0)     # 0 is between 0 and 50
number_range2(25)    # 25 is between 0 and 50
number_range2(50)    # 50 is between 0 and 50
number_range2(75)    # 75 is between 51 and 100
number_range2(100)   # 100 is between 51 and 100
number_range2(101)   # 101 is greater than 100
number_range2(-1)    # -1 is less than 0

