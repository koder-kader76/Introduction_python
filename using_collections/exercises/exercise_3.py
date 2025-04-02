# 3. Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).

original = (1, 2, 3, 4, 5)
length = len(original) - 1
duplicate = reversed(original[ 1:length ])
original = tuple(duplicate)
print(original)
# (4, 3, 2)

# ls:
#          -5 -4 -3 -2 -1
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]
print(result)