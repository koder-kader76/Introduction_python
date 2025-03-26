# floating point imprecision

# print(0.1 + 0.2)  # 0.3   # False
# 0.30000000000000004

import math
math.isclose(0.1 + 0.2, 0.3)    # True

# alternative
from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')           # True

# note use strings with decimal.Decimal
# e.g
print(Decimal(0.1) + Decimal(0.2))
# Decimal('0.3000000000000000166533453694')

