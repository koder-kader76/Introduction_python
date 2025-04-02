# 5. Which of the following values can't be used as a key in a dict object? Why?

'cat'                   # True
(3, 1, 4, 1, 5, 9, 2)   # True
['a', 'b']              # False
{'a': 1, 'b': 2}        # False
range(5)                # True
{1, 4, 9, 16, 25}       # False
3                       # True
0.0                     # True
frozenset({1, 4, 9, 16, 25}) # True

# values that can't be used as dic object keys
['a', 'b']  # list
{'a': 1, 'b': 2} # dict
{1, 4, 9, 16, 25} # set

# all 3 values are mutable - and non-hashable - python will raise an error when you try to create a dict object