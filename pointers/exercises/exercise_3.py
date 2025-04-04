# 3. Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# ans: 'The Life of Brian'
# dict2 is a shallow copy of dict1 - when shallow copies are made, the outermost level is duplicated and whatever is nested, will be referenced by both objects

# dict1 doesn't have any nested collections, so we can safely assume that dict1 & dict2 are 2 distinct objects which have the same values

# Since, they are two distinct objects, when dict2['Monty Python']'s value is rte-assigned, it does not affect the original dict1.