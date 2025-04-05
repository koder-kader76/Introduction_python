# import & from statements

import math

print(math.sqrt(math.pi))
# 1.7724538509055159

from math import pi, sqrt
print(sqrt(pi))
# 1.7724538509055159

# use an alias to avoid using math
import math as m

print(m.sqrt(m.pi))
# 1.7724538509055159


# the math module

import math
print(math.sqrt(36))    # 6.0
print(math.sqrt(2))     
# 1.4142135623730951

print(math.pi)          
# 3.141592653589793


# the datetime module

# import datetime from datetime class
# give the class an alias dt
from datetime import datetime as dt

# use strptime to create an instance of datetime.datetime class
date = dt.strptime("July 16, 2022", "%B %d, %Y")
weekday_name = date.strftime('%A')
print(weekday_name)
# Saturday

