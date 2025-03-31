# truthiness

# built-in falsy values
# False, None
# numeric 0, int, float, complex
# empty string ''
# empty collections: [], (), {}, set(), frozenset(), range(0)
# custom data types that evaluate to falsy

# e.g truthy value
value = 5
if 5:
    print(f'{5} is truthy')
else:
    print(f'{5} is falsy') 

# e.g falsy value
value = 0
if 0:
    print(f'{0} is truthy')
else:
    print(f'{0} is falsy') 

# Truthiness & short-circuit evaluation

# 'and' & 'or' operators care about the truthiness of their operands

# final value of the expression is value of the final sub expression evaluated by Python

print(3 and 'foo')  # last evaluated op: 'foo'
print('foo' and 3)  # last evaluated op: 3
print(0 and 'foo')  # last evaluated op: 0
print('foo' and 0)  # last evaluated op: 0

print(3 or 'foo')   # last evaluated op: 3
print('foo' or 3)   # last evaluated op: 'foo'
print(0 or 'foo')   # last evaluated op: 'foo'
print('foo' or 0)   # last evaluated op: 'foo'
print('' or 0)      # last evaluated op: 0
print(None or [])   # last evaluated op: []

# logical expressions that return non-boolean object

foo = None
bar = 'qux'
is_ok = foo or bar

# in the above example, is_ok is set to a truthy value 'qux'
# using a string as a boolean is not recommended

# e.g of using an if statement
foo = None
bar = 'qux'
if foo or bar:
    is_ok = True
else:
    is_ok = False

# alternative option:
is_ok = bool(foo or bar)