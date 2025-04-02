# adding elements to mutable sequences

# 3 methods - append, insert & extend

# seq.append - appends a single object to the end of mutable sequence

numbers = [1, 2]
numbers.append(10)
print(numbers)
# [1, 2, 10]


# insert - inserts an object into a mutable sequence before the element at a given index 
    # if index is greater than or equal to sequence length, object is appended to sequence
    # if index is a negative number, then it counts the index from the end of the sequence

numbers = [1, 2]

# seq.insert(index, object)

numbers.insert(0, 8)
print(numbers)
# [8, 1, 2]

numbers.insert(2, 6)
print(numbers)
# [8, 1, 2, 6]

numbers.insert(100, 55)
print(numbers)
# [8, 1, 2, 6, 55]

numbers.insert(-3, 33)
print(numbers)
# [8, 1, 2, 6, 55]
#  -5 -4 -3 -2 -1
# [8, 1, 33, 2, 6, 55]


# extend - appends the contents of a iterable sequence to the calling iterable

numbers = [1, 2]
numbers.extend([7, 8])
# Append 7 and 8 to numbers
print(numbers)
# [1, 2, 7, 8]