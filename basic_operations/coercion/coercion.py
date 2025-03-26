# coercion

# tyoe coercion

# strings to numbers
print(int('5'))                 # 5
print(float('3.141592'))        # 3.141592


# numbers to strings
print(str(5))                   # '5'
print(str(42))                  # '42'
print(str(3.141592))            # '3.141592'


# implicit coercion

# (Unnecessary) explicit coercion
print(str(3))           # '3'
print(str(False))       # 'False'
print(str([1, 2, 3]))   # '[1, 2, 3]'
print(str({4, 5, 6}))   # '{4, 5, 6}'

# Implicit coercion
print(3)                # '3'
print(False)            # 'False'
print([1, 2, 3])        # '[1, 2, 3]'
print({4, 5, 6})        # '{4, 5, 6}'

# print() will implicitly coerce any object into a string before printing it

 # implicit coercion occurs when mixing numeric values

 #      Type A      Type B      Result Type
 #      int         float       float
 #      int         Decimal     Decimal
 #      int         Fraction    Fraction
 #      float       Decimal     --error--
 #      float       Fraction    float
 #      Decimal     Fraction    --error--


 # gotchas from implicit coercion
print(True + True + True)           # 3
print(True + 1 + 1.0)               # 3.0
print(False * 50000)                # 0