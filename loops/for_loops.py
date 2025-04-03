# for loops

# for loops function the same way as while loops but they have a more condensed syntax
# advantages over a while loop
    # no initialization of variables
    # no conditional expression

# rewrite names loop

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

# example of a for loop iterating over a string

for char in 'Launch School':
    print(char)

# L
# a
# u
# n
# c
# h
 
# S
# c
# h
# o
# o
# l

#  same as above but with split() method
for word in 'Launch School'.split():
    print(word)

# Launch
# School

# use for loops with other collections

# looping over a set
my_set = {1000, 2000, 3000, 4000, 5000}
for member in my_set:
    print(member)

# 4000
# 2000
# 5000
# 3000
# 1000

# looping over a dictionary

# using a for loop with dictionary - defaults to using keys
my_dict = { 'a': 1, 'b': 2, 'c': 3 }
for key in my_dict:
    print(key)

# a
# b
# c

# use dict.values() for retrieving the values
my_dict = { 'a': 1, 'b': 2, 'c': 3 }
for value in my_dict.values():
    print(value)

# 1
# 2
# 3

# use dict.items() for retrieving key value pairs
my_dict = { 'a': 1, 'b': 2, 'c': 3 }
for item in my_dict.items():
    print(item)

# ('a', 1)
# ('b', 2)
# ('c', 3)


# use tuple unpacking to get both keys & values simultaneously

my_dict = { 'a': 1, 'b': 2, 'c': 3 }
for (key, value) in my_dict.items():
    print(f'{key} = {value}')

# a = 1
# b = 2
# c = 3

# same as above but without the parentheses which is more pythonic

my_dict = { 'a': 1, 'b': 2, 'c': 3 }
for key, value in my_dict.items():
    print(f'{key} = {value}')

# a = 1
# b = 2
# c = 3


# Nested Loops

# nested loops are often needed when there is more than one outer loop

# e.g deck of cards

suits = [
    'Clubs', 
    'Diamonds', 
    'Hearts', 
    'Spades',
]

ranks = [
    '2', '3', '4', '5', 
    '6', '7', '8', '9', 
    '10', 'Jack', 'Queen', 
    'King', 'Ace',
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)
