# key based access

# with dictionaries (mappings) use key-based access to retrieve the items in the dict - similar to indexing but it uses keys instead

# e.g

my_dict = {
    'a':    'abc',
    37:     'def',
    (5, 6, 7):  'ghi',
    frozenset([1, 2]): 'jkl',
}

# use strings, integers, tuples and frozensets as keys 
print(my_dict['a']) # 'abc'
print(my_dict[37])  # 'def'
print(my_dict[(5, 6, 7)])   # 'ghi'
print(my_dict[frozenset([1, 2])])   # 'jkl'

# when element is not found you get KeyError
# print(my_dict['nothing'])
# KeyError: 'nothing'

# use dict.get method - in case you anticipate getting a key error

# e.g
my_dict = {
    'a':    'abc',
    37:     'def',
    (5, 6, 7):  'ghi',
    frozenset([1, 2]):  'jkl',
}

print(my_dict.get('a'))     
# 'abc'
print(my_dict.get('nothing'))   
# None
print(my_dict.get('nothing', 'N/A'))
# 'N/A'
print(my_dict.get('nothing', 100))
# 100

# use key-base access to the left of the operator to re-assign values

my_dict = {
    'a':    'abc',
    37:     'def',
    (5, 6, 7):  'ghi',
    frozenset([1, 2]):  'jkl',
}

my_dict['a']    = 'ABC'
my_dict[37]     = 'DEF'
my_dict[(5, 6, 7)] = 'GHI'
my_dict[frozenset([1, 2])] = 'JKL'
print(my_dict)

# assign new keys to dicts
my_dict['xyz'] = 'Hey There!'
print(my_dict)
# {'a': 'ABC', 37: 'DEF', (5, 6, 7): 'GHI', frozenset({1, 2}): 'JKL', 'xyz': 'Hey There!'}

# keys must be immutable - Type Error for adding keys that are mutable

my_dict[[1, 2, 3]] = 'Hey There!'
# TypeError: unhashable type: 'list'