# logical operators

# not, and & or

# not
print(not True)     # False
print(not False)    # True
print(not(4 == 4))  # False
print(not(4 != 4))  # True

# and & or

#       A       B       A and B     A or B
#       True    True    True        True
#       True    False   False       True
#       False   True    False       True
#       False   False   False       False

# e.g 'and' operator
print((4 == 4) and (7 == 7))        # True
print((4 == 4) and (7 == 3))        # False
print((4 == 9) and (7 == 7))        # False
print((4 == 9) and (7 == 3))        # False

# e.g 'or' operator
print((4 == 4) or (7 == 7))         # True
print((4 == 4) or (7 == 3))         # True
print((4 == 9) or (7 == 7))         # True
print((4 == 9) or (7 == 3))         # False

# short circuits

# is_red(item) and is_portable(item)
# if the first expression is False, then python will terminate the program. it will short-circuit the entire expression as False

# is_green(item) or has_wheels(item)
# if the first expression returns True, the python will short-circuit the entire expression as True