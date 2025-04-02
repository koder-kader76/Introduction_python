# common collection operations

# non-mutating operations
# all operations work with mutating & non-mutating collections - never change the original collection - return a new object

# collection membership
# in operator - checks if the object on the operator's left is in the object of the operator's right
    # returns True if it is; False if not

# not in operator is the opposite of the in - returns False if the object is in the collection, True if not

# sequence & sets
    # compares objects for equality
# mappings
    # checks if the item is a key in dictionary
# strings
    # checks if the right string contains left string

seq = [4, 'abcdef', (True, False, None)]

print(4 in seq)                     # True
print(4 not in seq)                 # False
print('abcdef' in seq)              # True
print('abcdef' not in seq)          # False
print('cde' in seq[1])              # True
print('cde' not in seq[1])          # False
print('acde' in seq[1])             # False
print('acde' not in seq[1])         # True
print((True, False, None) in seq)   # True
print((True, False, None) not in seq)
# False
print(3.14 in seq)                  # False
print(3.14 not in seq)              # True

# minimum & maximum members
# returns the minimum & maximum members of a collection - the only requirement is that any pair of collections elements are comparable with '<' and '>'

my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
my_set2 = {'1', '4', '-9', '16', '25', '-36', '-1'}

print(min(my_set1), max(my_set1))
# -63, 25
print(min(my_set2), max(my_set2))
# -1, 4

# to compare 2 objects, min & max has to compare with the same type of objects
# min & max cannot be used with heterogenous collections

my_set = {1, 4, '-9', 16, '25', -36, -63, -1}
# print(min(my_set))
# TypeError: '<' not supported between instances of 'int' and 'str'
# print(max(my_set))
# TypeError: '<' not supported between instances of 'int' and 'str'

# possible to compare different types - between int & floats
numbers_set = {1, 3.14, -2.71}
print(min(numbers_set), max(numbers_set))
# -2.71 3.14

# use min/max with multiple args
print(min(3, 5, -1), max(3, 5, -1))


# summation
# sum function can be used with collections that only have numeric values - returns a sum of all the values summed up

numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(sum(numbers))

# Locating Indices & Counting

# index & count methods
# seq.index
    # returns the index of the first item that matches the object - returns ValueError
# seq.count
    # returns the number of times a value appears in a collection

names = ['Karl', 'Grace', 'Clare', 'Victor',
         'Antonina', 'Allison', 'Trevor']
print(names.index('Clare'))     # 2
print(names.index('Trevor'))    # 6
# print(names.index('Chris'))
# ValueError: 'Chris' is not in list

numbers = [1, 3, 6, 5, 4, 10, 1, 
           5, 4, 4, 5, 4]
print(numbers)
print(numbers.count(1))     # 2
print(numbers.count(3))     # 1
print(numbers.count(4))     # 4
print(numbers.count(7))     # 0

# index also works with strings - searches for the first matching substring of a string
names = 'Karl Grace Clare Victor Antonina Trevor'
print(names)
print(names.index('Grace'))         # 5
print(names.index('Antonina'))      # 24
print(names.index('John'))
# alueError: substring not found