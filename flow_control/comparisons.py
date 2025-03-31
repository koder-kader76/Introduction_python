# comparisons

# equality operator

print(5 == 5)       # True
print(5 == 4)       # False

print('abc' == 'abc')   # True
print('abc' == 'abcd')  # False

print(5 == '5')         # False

print([1, 2, 3] == [1, 2, 3])   # True
print([1, 2, 3] == [3, 2, 1])   # False

# operands must be same type & value to be equal

print(5 == float(5))        # True
big_num = 12345678901234567
print(float(big_num) == big_num)    # False

# comparisons - case-sensitive

print('abc' == 'aBc')   # False
print('abc'.lower() == 'aBc'.lower())  # True
print('abc'.upper() == 'aBc'.upper())  # True

# special cases - non-US alphabets
'straße'.lower() == 'strasse'.lower()  
# False
'straße'.casefold() == 'strasse'.casefold() 
# True


# inequality operator '!='

print(5 != 5)       # False
print(5 != 4)       # True
print('abc' != 'abc')   # False
print('abc' != 'aBc')   # True
print(5 != '5')         # True

# less than | less than equal to - '<' | '<='

print(4 < 5)        # True
print(5 < 4)        # False
print(5 < 5)        # False

print(4 <= 5)       # True
print(5 <= 4)       # False
print(5 <= 5)       # True

print('4' < '5')    # True
print('5' < '4')    # False
print('5' < '5')    # False

print('42' < '402') # False
print('42' < '420') # True
print('420' < '42') # False

# greater than | greater than or equal to
# '>' | '>='

print(4 > 5)        # False
print(5 > 4)        # True
print(5 > 5)        # False

print(4 >= 5)       # False
print(5 >= 4)       # True
print(5 >= 5)       # True

print('4' > '5')    # False
print('5' > '4')    # True
print('5' > '5')    # False

print('42' > '402') # True
print('42' > '420') # False
print('420' > '42') # True