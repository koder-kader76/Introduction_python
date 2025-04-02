# operations of dictionaries

# python provides 3 methods to get lists
    # dict.keys - retrieve keys
    # dict.values - retrieve values
    # dict.items = retrieve key/value pairs

people_phones = {
    'Chris':    '111-2222',
    'Pete':     '333-4444',
    'Clare':    '555-6666',
}

print(people_phones.keys())
# dict_keys(['Chris', 'Pete', 'Clare'])

print(people_phones.values())
# dict_values(['111-2222', '333-4444', '555-6666'])

print(people_phones.items())
# dict_items([('Chris', '111-2222'), ('Pete', '333-4444'), ('Clare', '555-6666')])

# dictionary view objects

# if you notice the output, the keys, values & items are wrapped in dict_keys(), dict_values() & dict_items()
    # these are not regular lists
    # they are dictionary view objects tied to the dictionary
    # if you add, update, remove any key value pair, these objects are updated accordingly


people_phones = {
    'Chris':    '111-2222',
    'Pete':     '333-4444',
    'Clare':    '555-6666',
}

keys = people_phones.keys()
values = people_phones.values()

print(keys)
# dict_keys(['Chris', 'Pete', 'Clare'])

print(values)
# dict_values(['111-2222', '333-4444', '555-6666'])

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)
# dict_keys(['Pete', 'Clare', 'Max'])

print(values)
# dict_values(['345-6789', '555-6666', '123-4567'])