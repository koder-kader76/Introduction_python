# str.capitalize - returns a copy of string with first character capitalized & remaining strings in lowercase

print("what's up?".capitalize())
# What's up?

print("456ABC".capitalize())
# 456abcs


# str.title - returns a copy of the string with every word being capitalized & remaining words lowercase

print("four SCORE and sEvEn".title())
# Four Score And Seven

print("four SCORE & sEvEn".title())
# Four Score & Seven

print("monty python's flying circus".title())
# Monty Python'S Flying Circus

# title is useful but it uses whitespace & certain punctuation to capitalize words


# capwords from string module uses only white space

import string
print(string.capwords("monty python's flying circus"))
# Monty Python's Flying Circus


# str.swapcase - returns a copy of a string with every uppercase changed to lowercase & vice versa

print("What's up".swapcase())
# wHAT'S UP

print('456ABC'.swapcase())
# 456abc

print('456ABC'.swapcase().swapcase())
# 456ABC

print('Straße'.swapcase().swapcase())   
# Strasse
# double swapcase() doesn't return the original string in non-unicode language