# what are sequences

# Sequences are types that maintain an ordered collection of objects (also: elements or values) that can be indexed by whole numbers.

letters = ['a', 'b', 'c']
print(letters[0])
print(letters[1])
print(letters[2])

# lists & tuples are heterogeneous - may contain multiple objects inlcuding other sequences

my_list = [
    'May',
    2.99,
    {None, True, False},
    [1, 2, 3],
]

# homogenous collections: range
# strings are considered homogenous text sequences

letters = ['a', 'b', 'θ', 'd', 'e']
char = letters[2]
print(char is letters[2])  # True
# both char & letters[2] ref the same obj


letters = 'abθde'
char = letters[2]
print(char is letters[2])   # False
# char & letters[2] are both distinct objects