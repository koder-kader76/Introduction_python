# return values

# all functions calls evaluate to a value
    # default value is None - implicit return value
    # use of return keyword - explicit return value

def add(a, b):
    return a + b

two_and_three = add(2, 3)
print(two_and_three)        # 5

# return statement
    # returns value to the code that invoked the function - returns None if no value is specified 
    # terminates the function and the returns control to the calling function

# predicates
    # function that return a Boolean value

# e.g
def is_digit(char):
    if char >= '0' and char <= '9':
            return True
    
    return False