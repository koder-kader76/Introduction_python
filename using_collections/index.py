# indexing

# process of using a whole number to access (& alter) elements in a sequence

# e.g
seq = ('a', 'b', 'c')
print(seq[0])   # 'a'
print(seq[1])   # 'b'
print(seq[2])   # 'c'
# print(seq[3]) # IndexError

# len function can be used to determine seq length
seq = ('a', 'b', 'c')
if len(seq) > 3:
    print(seq[3])

# access the last element of a sequence
seq = ('a', 'b', 'c')
last_index = len(seq) - 1
print(seq[last_index])

# use negative index to access the sequence from the back
seq = ('a', 'b', 'c')
print(seq[-1])  # 'c'
print(seq[-2])  # 'b'
print(seq[-3])  # 'a'

# change the value of an element
seq = ['a', 'b', 'c']
seq[1] = 'B'
print(seq)  # ['a', 'B', 'c']

# * above code mutates the list but re-assigns seq[1]