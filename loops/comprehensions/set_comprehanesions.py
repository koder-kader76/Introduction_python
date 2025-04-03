##############################################
# set comprehensions
##############################################

# set comprehensions are identical to dict comprehensions

# dict comprehension
# { key: value for element in iterable if condition }

# set comprehension
# { expression for element in iterable if condition }

# the only difference is the expression is a single value and not a key value pair
# the other difference is sets can only contain unique members so any duplicate values are not included

# basic example of a set comprehension
squares = { number * number 
           for number in range(1, 6) }

print(squares)
# {1, 4, 9, 16, 25}