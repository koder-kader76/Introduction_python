dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)

# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }


dict1['a'][1] = 42

# dict1 = {
#     'a': [1, 42, 3],
#     'b': (4, 5, 6),
# }

# dict2 = {
#     'a': [1, 42, 3],
#     'b': (4, 5, 6),
# }


print(dict2['a'])

# 4. Without running this code, what will it print? Why?

# [1, 42, 3]
# when dict2 = dict(dict1) - a shallow copy of the original dictionary is created. dict2 has a duplicate copy of the outermost level of dict1 and these are two distinct objects that are being reference by dict1 and dict2

# but dict1 & dict2 are still referencing the same objects within the nested level of the dictionary so when dict1['a'][1] is re-assigned to the integer object 42, dict2['a'] will reference the object's new state