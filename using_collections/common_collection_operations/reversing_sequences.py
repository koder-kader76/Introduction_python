# reverse sequences & dictionaries

# reversed function - reverse the order of elements in a sequence or dictionary
    # return value - lazy sequence 
    # to view the return value - use list/tuple constructor to iterate over the return value
    # don't use reversed if return value of a non-lazy sequence list or tuple is needed.

# list.reverse
    # this method can be used to reverse lists
    # this method mutates the list
        # use list.reverse when you don't need to preserve the original order
        # use reversed when only iterating over the list in reverse is needed
        
names = (
    'Grace', 
    'Clare', 
    'Allison', 
    'Trevor'
)

reversed_names = reversed(names)
print(reversed_names)
# <reversed object at 0x10535f220>

print(tuple(reversed_names))
# ('Trevor', 'Allison', 'Clare', 'Grace')
# reversed & printed tuple names

print(names)
# ('Grace', 'Clare', 'Allison', 'Trevor')
# original sequence unchanged

names = list(names)
print(names.reverse())
# None
# converted names to list & names.reverse()
# returned None - implies list mutated

print(names)
# ['Trevor', 'Allison', 'Clare', 'Grace']
# print names to confirm list mutated


# demonstrating reversed with dict
my_dict = {
    'a': 1,
    'xyz': 23,
    'pqr': 0,
    'jkl': 5,
}

reversed_dict = reversed(my_dict)
print(reversed_dict)
# <dict_reversekeyiterator object at 0x1010cd670>

print(list(reversed_dict))
# requires extra memory
# ['jkl', 'pqr', 'xyz', 'a


# practical usage of reversed - looping aid
# when iterating over a sequence in reverse is needed

names = (
    'Grace', 
    'Clare', 
    'Allison', 
    'Trevor'
)

for name in reversed(names):
    print(name)
# Trevor
# Allison
# Clare
# Grace