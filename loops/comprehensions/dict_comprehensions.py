############################################
# dictionary comprehensions
############################################

# dictionary comprehensions are identical to list comprehensions but in this instance, they create new dictionaries
# syntax difference, use curly braces {}
# expression uses key: value pair

# example code
# { key: value for element in iterable if condition }

# basic example of dictionary comprehension

squares = { f'{number}-squared': 
           number * number 
           for number in range(0, 6) }

print(squares)
# {
#   '0-squared': 0, 
#   '1-squared': 1, 
#   '2-squared': 4, 
#   '3-squared': 9, 
#   '4-squared': 16,
#   '5-squared': 25,
# }

