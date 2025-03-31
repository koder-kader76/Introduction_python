# sequence constructors

# constructors - special program to create new objects - can only use constructors to create ranges, lists, frozensets and empty sets

# string constructor
str()               # '' (empty string)
str('abc')          # 'abc'
str(42)             # '42'
str(3.141592)       # '3.141592'
str(False)          # 'False
str(range(3, 7))    # 'range(3, 7)'
str([1, 2, 3])      # '[1, 2, 3]'
str(int)            # '<class int>'
str(list)           # '<class list>'

class Person: pass
str(Person())       
# '<__main__.Person object at 0x101174980>'


# range constructor - 3 forms
# range(start, stop, step)
r = range(5, 12, 2)
print(list(r))      # [5, 7, 9, 11]

r = range(12, 8, -1)
print(list(r))      # [12, 11, 10, 9]

r = range(12, 5, -2)
print(list(r))      # [12, 10, 8, 6]

# create empty ranges 
# where start >= stop when step is positive
r = range(8, 5, 1)
print(list(r))

# where start <= stop when step is negative
r = range(5, 7, -1)
print(list(r))

# range(start, stop)
# when you omit the step, python uses the default 1

# range(stop)
# when you don't specify start value, python uses 0 by default

# ranges are lazy sequences - they do not produce any output - need to use list, tuple to view them

# list, tuple, set, frozenset constructors

# list()    |       list(iterable)
# tuple()   |       tuple(iterable)
# set()     |       set(iterable)
# frozenset() |     frozenset(iterable)

my_str = 'Python'

my_list = list(my_str)
print(my_list)  
# ['P', 'y', 't', 'h', 'o', 'n']

my_tuple = tuple(my_str)
print(my_tuple)
# ('P', 'y', 't', 'h', 'o', 'n')

my_set = set(my_str)
print(my_set)
# {'h', 'o', 'y', 'P', 't', 'n'}


# use constructors to duplicate collection
my_list = [5, 12, 2]
another_list = list(my_list)

print(my_list)
# [5, 12, 2]

print(another_list)
# [5, 12, 2]

print(my_list == another_list)
# True

print(my_list is another_list)
# False

# e.g of duplicate nested list
nested_list = [[1, 2, 3], [4, 5, 6]]
dup_nested_list = list(nested_list)

print(nested_list)
# [[1, 2, 3], [4, 5, 6]]

print(dup_nested_list)
# [[1, 2, 3], [4, 5, 6]]

print(nested_list == dup_nested_list)
# True

print(nested_list is dup_nested_list)
# False

print(nested_list[0] is dup_nested_list[0])
# True

print(nested_list[1] is dup_nested_list[1])
# True

# nested_list are different objects to dup_nested_list but it's elements are the same

# python make a shallow copy for nested lists

# passing a string to any of the above constructors causes them to iterate over the characters to create a new collection

print(tuple('Python'))
# ('P', 'y', 't', 'h', 'o', 'n')