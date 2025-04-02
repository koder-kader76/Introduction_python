# merging collections

# zip
    # works with all iterables
    # merge members of multiple iterables into a single list of tuples
    # easy to iterate through many collections simultaneously

# example
iterable_1 = [1, 2, 3]
iterable_2 = ('Kim', 'Leslie', 'Bertie')
iterable_3 = [None, True, False]

zipped_iterables = zip(iterable_1, iterable_2, iterable_3)

# zip's return value is a lazy sequence
    # explicitly request values using iterator constructor
print(list(zipped_iterables))

# [
#   (1, 'Kim', None), 
#   (2, 'Leslie', True), 
#   (3, 'Bertie', False)
# ]

# zip's collection arguments length is usually the same but you can add a strict=True keyword argument to the invocation

# example
zipped_iterables = zip(
    iterable_1, 
    iterable_2, 
    iterable_3, 
    strict=True,
)

print(list(zipped_iterables))

# case study: in the event, lengths differ and strict=True not given, zip stops iterating after the shortest iterable

# example
result = zip(
    range(5, 10),   # length is 4
    range(1, 3),    # length is 2 (shortest)
    range(3, 7),    # length is 3
)

print(list(result))
# [(5, 1, 3), (6, 2, 4)]

# zip returns what is known as an iterator
    # once an iterator object has been iterated over, subsequent attempts to iterate over the object will fail
print(list(result))
# []



result = zip(
    range(5, 10),   # length is 4
    range(1, 3),    # length is 2 (shortest)
    range(3, 7),    # length is 3
)

zipped_result = list(result)
print(zipped_result)
print(zipped_result)
