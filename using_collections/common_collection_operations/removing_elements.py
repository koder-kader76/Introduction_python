# removing elements from a mutable sequence

# 3 ways - remove, pop & clear

# remove - seq.remove searches for a object and removes the first occurence of that object
    # if object not found, raises ValueError

my_list = [2, 4, 6, 8, 10]

my_list.remove(8)
print(my_list)
# [2, 4, 6, 10]

# my_list.remove(8)
# ValueError: list.remove(x): x not in list

# pop - syntax: seq.pop(index)
    # removes & returns index element
    # if no index given, by default last element removed
    # raises error is index is out of range
    # only works for mutable indexed sequences

my_list = [2, 4, 6, 8, 10]

print(my_list.pop(1))
# 4
print(my_list)
# [2, 6, 8, 10]
print(my_list.pop())
# 10
print(my_list)
# [2, 6, 8]

# print(my_list.pop(4))
# IndexError: pop index out of range


# clear - syntax: seq.clear()
    # removes all elements from a sequence

my_list = [2, 4, 6, 8, 10]

my_list.clear()
print(my_list)
# []