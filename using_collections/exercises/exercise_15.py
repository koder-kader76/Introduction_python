pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# 15. Without running the following code, what values will be printed by line 10?

# dict_keys(['Cat', 'Bird', 'Snake'])