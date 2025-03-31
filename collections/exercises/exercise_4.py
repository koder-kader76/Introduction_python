# 4. Why can we treat strings as sequences?

# a) strings, except for empty strings, behave the same way as collections.
# a program will be able to iterate through the individual characters as elements in a list or tuple

# e.g 
text = 'abcdefghi'
for char in text:
    print(char)
# a
# b
# c
# d
# e
# f
# g
# h
# i

# b) access any item within index numbers
print(text[0])  # 'a'
print(text[1])  # 'b'

