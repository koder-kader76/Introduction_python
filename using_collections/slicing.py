# slicing

# indexing also supports slicing augmentation - slicing can extract (or modify) any number of consecutive elements simultaneously

# syntax
# seq[ start : stop ] - retrives elements between start & stop - 1

# index      0  1  2  3  4  5  6  7  8
# seq =     'a  b  c  d  e  f  g  h  i'
# -index    -9 -8 -7 -6 -5 -4 -3 -2 -1

# 3 ways to perform a slicing operation
# seq[start:stop]
    # gets elem from start to stop -1
# seq[-start:-stop]
    # gets elem from -start to -stop +1
# seq[start:stop:step]
    # gets elem from start to stop -1 with every step elem


# e.g slicing with a string - returns a string
# index      0  1  2  3  4  5  6  7  8
# seq =      a  b  c  d  e  f  g  h  i
# -index    -9 -8 -7 -6 -5 -4 -3 -2 -1


seq = 'abcdefghi'
print(seq[3:7])     # 'defg'
print(seq[-6:-2])   # 'defg'
print(seq[2:8:2])   # 'ceg'
print(repr(seq[3:3]))   # ''
# returns empty string when start/stop are the same values
print(seq[:])       # 'abcdefghi'
# returns duplicate sequence - a shallow copy
print(seq[::-1])    # 'ihgfedcba'
# returns reversed copy of sequence - similar to seq.reverse()
# seq[::-1] returns new sequence - seq.reverse() mutates the original sequence


# e.g slicing with a list - returns list
# index    0  1  2  3  4  5  6  7  8  9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# -index -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(numbers[3:7])     # [4, 5, 6, 7]
print(numbers[-6:-2])   # [5, 6, 7, 8]
print(numbers[2:8:2])   # [3, 5, 7]
print(numbers[3:3])     # []
print(numbers[:])       
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::-1])
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

nested_list = [[1, 2], [3, 4]]
nested_list_dup = nested_list[:]
print(nested_list[0] is nested_list_dup[0])
# True
# nested_list_dup is a duplicate copy which is a shallow copy of the original