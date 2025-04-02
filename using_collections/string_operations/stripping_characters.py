# stripping characters

# str.strip - returns a copy of string by stripping all the trailing whitespace

# example
# text = input().strip()

# example
text = ' \t   abc def         \n\r'
print(repr(text))
#  ' \t   abc def         \n\r'

print(repr(text.strip()))
# 'abc def'

# pass in arguments to remove other characters
text = ' \t   abc def         \n\r'
print(repr(text.strip('abc')))
# ' \t   abc def         \n\r'

text = 'aaabaacccabxyzabccba'
print(text.strip('a'))
# baacccabxyzabccb
print(text.strip('ab'))
# cccabxyzabcc
print(text.strip('ba'))
# cccabxyzabcc
print(text.strip('abc'))
# xyz
print(text.strip('bc'))
# aaabaacccabxyzabccba

print(repr(text.strip('abcxyz')))
# ''

# str.lstrip() - removes leading characters (the leftmost)
# str.rstrip() - removes trailing characters (the rightmost)

text = 'aaabaacccabxyzabccba'

print(text.lstrip('a'))
# baacccabxyzabccba
print(text.rstrip('a'))
# aaabaacccabxyzabccb

print(text.lstrip('ab'))
# cccabxyzabccba
print(text.rstrip('ab'))
# aaabaacccabxyzabcc

print(text.lstrip('ba'))
# cccabxyzabccba
print(text.rstrip('ba'))
# aaabaacccabxyzabcc

print(text.lstrip('abc'))
# xyzabccba
print(text.rstrip('abc'))
# aaabaacccabxyz