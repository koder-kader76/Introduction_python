# Sets

# create a set from a literal
s2 = {2, 3, 5, 7, 11, 13}
print(s2) # {2, 3, 5, 7, 11, 13}

# create a set from a string
s3 = set('hello there!')
print(s3) # {'t', 'o', 'e', 'l', ' ', 'h', '!', 'r'}

# create a empty set
s1 = set()
print(s1) # set()

# create with empty literal curly braces
d1 = {}
print(type(d1)) # <class 'dict'>

# multi-line format set
monty_python_cast = {
    'Eric Idle',
    'John Cleese',
    'Terry Gilliam',
    'Graham Chapman',
    'Michael Palin',
    'Terry Jones',
}

# 2 main type of sets
# sets & frozensets
# frozensets are immutable

s5 = frozenset([1, 2, 3])
print(s5)

s6 = frozenset((1, 2, 3))
print(s6)

s7 = frozenset({1, 2, 3})
print(s7)

s8 = frozenset(range(1, 4))
print(s8)