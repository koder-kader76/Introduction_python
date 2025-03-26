# arithmetic operations

# +     addition
# -     subtraction
# *     mutliplication
# /     division
# //    integer division
# %     modulo
# **    exponentiation

# above mentioned - work with integers, floats & other complex numeric values but perform similar operations with other data types

# addition (+)

print(38 + 4)   # 42
print(38.4 + 41.9)  # 80.3

# mixing integers & floats
print(38 + 41.5)    # 79.5


# subtraction

print(38 - 4)       # 34
print(38.4 - 41.9)  # -3.5

# mixing integers & floats
print(38 - 41.5)    # -3.5


# multiplication
print(38 * 4)       # 152
print(38.4 * 41.1)  # 1578.24

# mixing integers & floats
print(38 * 41.5)    # 1577.0


# division (/)

print(16 / 4)
print(16 / 2.5)

# return value always a float


# integer division

print(16 // 3)          # 5
print(16 // -3)         # -6
print(16 // 2.3)        # 6.0
print(-16 // 2.3)       # -7.0

# int division returns result nearest to whole number
# rounds down to the nearest whole number
# doesn't work with built-in complex numbers


# exponentiation

# 3**4  - 3 * 3 * 3 * 3
# 3 to the power of 4
print(3**4)     # 81
print(16**3)    # 4096
print(2**5)     # 32
print(2**1)     # 2
print(2**0)     # 1


# modulo operator (%)

# calculates remainder of dividing 2 integers

print(15 % 3)   # 0
print(16 % 3)   # 1
print(17 % 3)   # 2
print(18 % 3)   # 0

# e.g a & b positive integers
# a % b returns non-negative remainder
print(17 / 7)    # 3 

# a % b return 0 if a is divisble by b
print(14 / 7)    # 0

# if either a or b is negative, the output can be unexpected
print(17 / -7)  # -4
print(-17 / 7)  # 4

# table
#   a       b       a % b   remainder
#   14      7       0       0
#   17      7       3       3
#   17      -7      -4      3
#   -17     7       4       -3
#   -17     -7      -3      -3

from math import remainder

print(int(remainder(14, 7)))     # 0
print(int(remainder(17, 7)))     # 3
print(int(remainder(17, -7)))    # 3
print(int(remainder(-17, 7)))    # -3
print(int(remainder(-17, -7)))   # -3

# if a % b == 0; a & b signs irrelevant

