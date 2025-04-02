# nested collections

# collections can be nested inside other collections

# example is a list that contains a dict, tuple, set, and another list
nested_list = [
    {'foo': 42, 'bar': [1, 2, 3], 'qux': None },
    {
        'Kim',
        ('Leslie', 'Les'),
        ('Pete', 'Peter'),
        ('Jonathan', 'Jon', 'Jack'),
    },
    (4, 5, (1, 2, 3), 6, 7),
    ['a', 'b', 'cde', -3.141592],
]

# limitations of nesting collections
# can't nest a mutable collection list, dictionary or set inside of a set
# example

# my_set = {1, 2, 3, [4, 5]}
# TypeError: unhashable type: 'list'

# my_set = {1, 2, 3, {4, 5}}
# TypeError: unhashable type: 'set'

# my_set = {1, 2, 3, {'4': 5}}
# TypeError: unhashable type: 'dict'

# nesting a frozenset inside a set or frozenset is possible
my_set = {1, 2, 3, frozenset([4, 5])}
print(my_set)
# {frozenset({4, 5}), 1, 2, 3}

# nesting mutable collection within tuples is also possible
my_tuple = (
    1, 
    2, 
    3, 
    [4, 5], 
    {6, 7}, 
    {'x': 'a dict'},
)
print(my_tuple)
# (1, 2, 3, [4, 5], {6, 7}, {'x': 'a dict'})

# nested collections
    # need some sense of structure and reasoning

# e.g create a deck of cards

deck = [
    {'suit': 'Clubs', 'value': '2'},
    {'suit': 'Clubs', 'value': '3'},
    {'suit': 'Clubs', 'value': '4'},
    {'suit': 'Spades', 'value': 'Queen'},
    {'suit': 'Spades', 'value': 'King'},
    {'suit': 'Spades', 'value': 'Ace'},
]

# to print the fiftieth card, we can write
# print(f"{deck[49]['value']} of {deck[49]['suit']}")
# Queen of Spades

# several layers of nesting in a sequence
# access any item from any nested part of
# of the sequence

nested_seq = [
    [1, 2, [3, 4, (5, 6, 7, 8)]],
    [9, [10, (11,)]],
    [12, 13, [14, 15, (16, 17)]],
    [18, [19, 20, (21, 22)]],
]

print(nested_seq[1]) 
# [9, [10, (11,)]]
print(nested_seq[3][0])
# 18
print(nested_seq[0][2][2])
# (5, 6, 7, 8)
print(nested_seq[2][2][2][1])
# 17