# sets

# Sets are types that maintain an unordered collection of unique objects (also called elements or members). Unlike sequences, sets cannot be indexed.

# 2 types: sets & frozensets
# difference: sets are mutable - frozensets are immutable

letters = {'a', 'b', 'c'}
letters.add('d')
print(letters)
# {'b', 'a', 'c', 'd'}

frozen_letters = frozenset(letters)
# frozen_letters.add('e')
# AttributeError: 'frozenset' object has no attribute 'add'

# sets & frozensets are heterogeneous - contain different types of objects, including other hashable collections

my_set = {
    'May',
    2.99,
    (None, True, False),
    range(5),
}

# if duplicate members are added, python will ignore them

letters = {'a', 'b', 'c', 'd', 'a'}
print(letters)
# {'d', 'b', 'a', 'c'}

letters.add('c')
print(letters)
# {'d', 'c', 'b', 'a'}

# frm python 3.7, integer sets seem to be ordered
numbers = { 1, 2, 3, 4, 5 }
print(numbers)
# {1, 2, 3, 4, 5}

numbers = { 5, 3, 1, 2, 4}
print(numbers)
# {1, 2, 3, 4, 5}

# behavior isn't guaranteed
numbers = { 1, 2, 37, 4, 5 }
print(numbers)
# {1, 2, 4, 37, 5}