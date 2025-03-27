# examples of print function

# print function
    # works often with all data types
    # output focus for human readability 

print({
    'a': 1,
    'b': 42,
    'c': "string",
    'd': [5, 6],
    'e': { 8, 9, 10 },
})
# {'a': 1, 'b': 42, 'c': 'string', 'd': [5, 6], 'e': {8, 9, 10}}

import time
print(time.asctime())
# Thu Mar 27 16:59:55 2025

# print multiple objects in print function'
print(1, 2, 3, 'a', 'b')
# 1 2 3 a b

print(
    [1, 2, 3],
    4,
    False,
    {5, 6, 7, 8},
)
# [1, 2, 3] 4 False {8, 5, 6, 7}

# default separation - space (' ')
# use sep keyword to modify default separator

print(1, 2, 3, 'a', 'b', sep=',')
# 1,2,3,a,b

print('a', 'b', 'c', 'd', 'e', sep='')
# abcde

# end keyword print() prints after it prints the last arg
    # common reasons
        # windows compatiblity - needs newline
        # suppressing newline altogether

# explicitly stating print fn needs newline
# when running windows env (\r\n)
print(1, 2, 'a', 'b', sep=',', end=' <-\n')

# suppressing newline altogether - end=""
print('a', 'b', end='', sep=','); print('c', 'd', sep=',')

# to start new line immediately
print()