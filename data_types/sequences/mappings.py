# dictionaries

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

print(my_dict) 
# {'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}

# access individual elements
my_dict['cat']
# meows

my_dict['bird']
# KeyError

# index re-assignment
my_dict['cat'] = "purrs"
# {'dog': 'barks', 'cat': 'purrs', 'pig': 'oinks'}

# dictionary literals may also use multi-line format

monty_python = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',
    ],
    'first_season': 1969,
    'last_season': 1974,
    'reboot_season': None,
}


# empty dic
new_dict = {}
new_dict['a'] = 1
new_dict['b'] = 2
print(new_dict)     # {'a': 1, 'b': 2}
del new_dict['a']
new_dict['a'] = 1
print(new_dict)     # {'a': 1, 'b': 2}