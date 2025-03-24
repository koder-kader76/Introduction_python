# Indexing Strings

# acces individual char of string wiht []

my_str = 'abc'
print(my_str[0])
print(my_str[1])
print(my_str[2])
print(my_str[3]) # IndexError: string index out of range

# using negative numbers
print(my_str[-1]) # c
print(my_str[-2]) # b
print(my_str[-3]) # a
print(my_str[-4]) # IndexError: string index out of range

# print my_str backwards
print(my_str[::-1]) # 'cba'