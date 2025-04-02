# 2. Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

# initialize name variable to 'Launch School'
name = 'Launch School'

# determine the index of the first c with str.find
index_c = name.find('c')
print(index_c)  # 4

# print a 6-character substring from name
print(repr(name[index_c:index_c + 6]))
# 'ch Sch'

