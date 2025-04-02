# comparing collections

# python supports comparison operations for all collections

# equality is the most straightforward comparison if two collections meet all of the following requirements
    # they have the same type; sets & frozensets are considered the same 
    # they have the same number of elements
    # for sequences, each pair of corresponding elements compares as equal
    # for sets, each set has the same members
    # for mappings, each key/value pair is present & identical in both mappings (order does not matter)

print([2, 3] == [2, 3])     # True
print([2, 3] == [3, 2])     # False
print([2, 3] == [2])        # False
print([2, 3] == (2, 3))     # False
print({2, 3} == {3, 2})     # True

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
dict3 = {'a': 1, 'b': 2, 'c': 3}

print(dict1 == dict2)   # True
print(dict1 == dict3)   # False