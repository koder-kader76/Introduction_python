# string representations

# str() & repr()

my_str = 'abc'
print(my_str)           # abc
print(str(my_str))      # abc
print(repr(my_str))     # 'abc'

# The str() output shows the date in a format that's easy for humans to read

# The repr() function is particularly useful during debugging when you need to see the exact structure and values of objects in your code.

import datetime

today = datetime.datetime.now()
print(str(today))  # 2025-03-25 19:24:47.997280
print(repr(today)) # datetime.datetime(2025, 3, 25, 19, 24, 47, 997280)