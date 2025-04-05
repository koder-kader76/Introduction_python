# function composition

 # Function composition occurs when a function call is used as an argument to another function call which may be in turn used as another function call

# in each case, the return value of the inner function is used as an argument to the outer function

# example
print(list(range(3, 17, 4)))

# add & subtract functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

sum = add(20, 45)
print(sum)

difference = subtract(80, 10)
print(difference)

# common way to use function composition
print(add(20, 45))
print(subtract(80, 10))

# in the above example, the function call is used on the print function


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def times(num1, num2):
    return num1 * num2

print(times(add(20, 45), subtract(80, 10)))
# 4550

# above code produces the same value as the one below
total = add(20, 45)
difference = subtract(80, 10)
result = times(total, difference)
print(result)
# 4550

