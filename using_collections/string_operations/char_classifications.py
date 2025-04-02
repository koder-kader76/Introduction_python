# character classification

# str.isalpha() - return True if all characters are alphabets & False otherwise

print('Hello'.isalpha())
# True
print('Good-bye'.isalpha())
# False
print('Four score'.isalpha())
# False
print(''.isalpha())
# False


# str.isdigit() - returns True if all characters are digits otherwise False
    # empty string is False

print('12340'.isdigit())
# True
print('123.4'.isdigit())
# False '.' is not digit
print('-1234'.isdigit())
# False '-' is not digit
print(''.isdigit())
# False

# str.isalnum() - True if str is composed entirely of letters and/or digits
    # returns False if the string is empty

# str.islower() - True if all cased characters in str are lowercase letters, False otherwise
    # returns False if the string contains no case characters

# str.isupper() -  True if all cased characters in str are uppercase, False otherwise
    # returns False if the string contains no case characters

# str.isspace() - True if all characters in str are whitespace characters, False otherwise
    # returns False if the string is empty
    # whitespace characters include
        # whitespace( )
        # tabs (\t)
        # newlines (\n)
        # carriage return (\r)
        # vertical tabs (\v)
        # form feeds (\f)

# all the above methods are unicode aware
# 'Καλωσήρθες'.isalpha() # True

# use this to exclude non-ascii characters
# text.isalpha() and text.isascii()