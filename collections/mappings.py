# mappings

# Mappings are types that maintain an unordered collection of key/value pairs (also called elements or members). Unlike sequences, mappings are accessed by their keys, which usually are not numbers.

example = {
    'a': 1, 
    (1, 3): 3, 
    1: 'x',
}

print(example) # {'a': 1, (1, 3): 3, 1: 'x'}
print(example['a']) # 1
print(example[(1, 3)])  # 3
print(example[1])   # x

example['a'] = 'A'
print(example) # {'a': 'A', (1, 3): 3, 1: 'x'}

# dicts are by default unordered collections - but you can rely on ordering in the context where insertion matters

d = {
    'a': 1,
    (1, 3): 3,
    1: 'x',
}

del d['a']
print(d)    
# {(1, 3): 3, 1: 'x'}

d['a'] = 42
print(d)
# {(1, 3): 3, 1: 'x', 'a': 42}