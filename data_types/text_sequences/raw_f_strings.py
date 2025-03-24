# raw & f-strings

# raw strings

# both of these will print C:\Uses\Xyzzy
print("C:\\Users\\Xyzzy")
print(r"C:\Users\Xyzzy")

# when to use raw strings
# - with Win Style file names
# - with regular expressions

# f-strings
# formatted string literals / f-strings

# string interpolation

print(f'5 plus 5 equals {5 + 5}') 
# '5 plus 5 equals 10.'

my_name = "Karl"
print(f'My name is {my_name}.')

my_name = 'Clare'
greeting = 'Ey up?'
print(f'{greeting} My name is {my_name}.')

# if literal {} is needed - use double
foo = 'hello'
print(f'Use {{foo}} to embed a string: {foo}')

# two more f-string variants for integers
print(f'{123456789:_}') # 123_456_789
print(f'{123456789:,}') # 23,456,789

# f-string on floating point number
print(f'{123456789.7890123:_}') # 123_456.7890123
print(f'{123456789.7890123:,}') # 123,456.7890123