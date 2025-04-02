# startswith & endswith

# str.startswith - returns True if string given by str begins with certain substring, False otherwise

print('Four score and seven'.startswith('Four score'))
# True
print('Four score and seven'.startswith('For score'))
# False
print('Four score and seven'.startswith('score'))
# False

# argument can also be a tuple of strings
print('abc def'.startswith(('abc', 'xyz', 'stu')))
# True
print('def ghu'.startswith(('abc', 'xyz', 'stu')))
# False
print('xyz uvw'.startswith(('abc', 'xyz', 'stu')))
# True
print('stu vwx'.startswith(('abc', 'xyz', 'stu')))
# True

# method also accepts start and end indexes to dictate where the search begins
print('abc def'.startswith('def', 4))
# True
print('abc def ghi'.startswith('def', 4, 7))
# True


# str.endswith - returns True if the string given by str ends with a certain substring, False if it does not

print('Four score and seven'.endswith('and seven'))
# True
print('Four score and seven'.endswith('ad seven'))
# False
print('Four score and seven'.endswith('score'))
# False


# argument can also be a tuple of strings
print('abc def'.endswith(('abc', 'xyz', 'stu')))
# False
print('abc def'.endswith(('xyz', 'def')))
# True

# method also accepts start and end indexes to dictate where the search begins
print('abc def'.endswith('def', 4))
# True
print('abc def ghi'.endswith('def', 4, 7))
# True