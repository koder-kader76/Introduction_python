# examples of floats - floating point data type (float)

one = 1.0
pi_third = 1.4142
negative_pi = -3.141592
large_float = 42348.912346
extra_large_float = 131_587_465.014_410_491
extra_large_float2 = 131587465.014410491

# large numbers in floats cannot be represented by comma(,) or period(.)
# as with integers - use underscore or no spaces

# Working with Big & Small Floats (optional)

import sys
# the maximum number of digits that can be shown
print(sys.float_info.dig) # Typically 15

# the largest possible positive float value
print(sys.float_info.max)  # About 1.8 * (10**308)

# The smallest non-zero positive float value
print(sys.float_info.min) # About 2.2 * (10**-308)

# python prints extremely large & small floats using scientific notation
print(3.14 * (10**20)) # 3.14e+20
print(3.14* (10**-20)) # 3.14e-20

# use scientific notation when writing floats
print(3.14e+20 / 2.72e-15) # 1.1544117647058823e+35

# use scientific notation - large integer (use int)
print(3 * (10**20)) # 300000000000000000000

print(int(3e+20))   # 300000000000000000000