#############################################
# comprehensions
#############################################

# comprehensions - create a mutable collection from an exising iterable collection

# 3 types of comprehension:
#   lists
#   dictionaries
#   sets

# comprehensions are expressions
    # used on the right side of an argument
    # as a function argument
    # return value
    # any place where an expressison evaluates as a list, dict, or set
    # used as standalone expressions


##############################################
# Why No Tuple, Range, or String Comprehensions?
##############################################

# result = empty_collection               # [], {}, set()
# for item in collection:
#     result.append(item)

# comprehensions don't build their results all at once
# it's a process that is built like above mentioned code

# since tuples, ranges and strings are immutable, comprehensions cannot start building comprehensions