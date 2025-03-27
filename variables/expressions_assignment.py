# expressions & assignment

# assignment & reassignment - use expressions to the right of '=' to determine desired value

#e.g.
left_side = 5
right_side = 32
total = left_side + right_side  # total = 37
print(total)                    # prints 37

# e.g using function call
def square(number):
    return number * number

forty_two_squared = square(42)
print(forty_two_squared)        # 1764

# note: the right side of an assignment is completely evaluated before assigning the result to the desired variable

foo = 42            # foo is 42
foo = foo - 2       # foo is now 40
foo = foo * 3       # foo is now 120
foo = foo + 5       # foo is now 125
foo = foo // 25     # foo is now 5
foo = foo / 2       # foo is now 2.5
foo = foo**3        # foo is now 15.625
print(foo)