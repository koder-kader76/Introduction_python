# built-in functions

# min and max
print(min(-10, 5, 12, 0, -20))      # -20
print(max(-10, 5, 12, 0, -20))      # 12

print(min('over', 'the', 'moon'))   # moon
print(max('over', 'the', 'moon'))   # the

# print(max(-10, '5', '12', '0', -20))
# TypeError: '>' not supported between instances of 'str' and 'int'

my_tuple = ('i', 'tawt', 'i', 'taw', 'a', 'puddy', 'tat')
print(min(my_tuple))    # a
print(max(my_tuple))    # tawt


# ord & chr

# ord
print(ord('a'))         # 97
print(ord('A'))         # 65
print(ord('='))         # 61
print(ord('~'))         # 126

# chr
print(chr(97))          # 'a'
print(chr(65))          # 'A'
print(chr(61))          # '='
print(chr(126))         # '~'

# Truthy & Falsy

# Falsy values
# False, None
# numeric value: 0
    # integer
    # float
    # complex
# empty strings: ''
# empty collecitions: 
    # list: []
    # tuple: ()
    # dict: {}
    # set: set()
    # frozenset: frozenset()
    # range(0)
# custom data types

# rest of data type - Truthy


# any & all

collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))     # False
print(any(collection2))     # True
print(any(collection3))     # True
print(any([]))              # False

print(all(collection1))     # False
print(all(collection2))     # False
print(all(collection3))     # True
print(all({}))              # True

# using comprehensions for any & all
numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers])
# [True, False, True, True, False]

numbers = [2, 5, 8, 10, 13]
print(any([number % 2 == 0 for number in numbers]))
# True

print(all([number % 2 == 0 for number in numbers]))
# False

numbers_2 = [5, 13]
print(any([number % 2 == 0 for number in numbers_2]))
# False

print(all([number % 2 == 0 for number in numbers_2]))
# False

numbers_3 = [2, 8, 10]
print(any([number % 2 == 0 for number in numbers_3]))
# True

print(all([number % 2 == 0 for number in numbers_3]))
# True