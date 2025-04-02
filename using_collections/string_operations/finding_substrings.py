# search through strings to find a substring

# str.find & str.rfind

# str.find - looks for first occurence of argument 
# str.rfind - sames as str.find but starts from the right
# the return value is the index of the first matching string; otherwise -1 is returned

school = 'launch school'

print(school.find(' '))     # 6
print(school.find('l'))     # 0
print(school.find('h'))     # 5
print(school.find('hoo'))   # 9
print(school.find('x'))     # -1
print(school.find('N'))     # -1


print(school.rfind(' '))     # 6
print(school.rfind('l'))     # 12
print(school.rfind('h'))     # 9
print(school.rfind('hoo'))   # 8
print(school.rfind('oh'))    # -1

# str.find is case-sensitive, 'N' does not match
print(school.rfind('N'))     # -1


# use slices of a string by adding start & end indices to str.find

text = 'abc abc def abc'

print(text.find(' ', 4))    # 7
print(text.find(' ', 8))    # 11

print(text.find('c', 0, 2)) # -1
print(text.find('c', 3, 10))    # 6


# note:
# using str.find or str.rfind is not the same as using [start:stop] syntax first

# example
text = 'abc abc def abc'

print(text[3:10].find('c'))     # 3
print(text.find('c', 3, 10))    # 6

# when slicing arguments are used, the method considers the starting point of the string before returning the index of the substring
# when you use [start:stop] syntax, it creates a new copy of the string and the substring index will follow that of the copy and not the original string