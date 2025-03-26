# ordered comparisons

# less than (<) less than or equal (<=)

print(42 < 41)      # False
print(42 < 42)      # False
print(42 <= 42)     # True
print(42 < 43)      # True

print('abcdf' < 'abcef')    # True
print('abc' < 'abcdef')     # True
print('abcdef' < 'abc')     # False
print('abc' < 'abc')        # False
print('abc' <= 'abc')       # True
print('abd' < 'abcdef')     # False
print('A' < 'a')            # True
print('Z' < 'a')            # True

print('3' < '24')           # False
print('24' < '3')           # True

# string comparison takes place lexicographically


# more than (>) more than or equal (>=)

print(42 > 41)      # True
print(42 > 42)      # False
print(42 >= 42)     # True
print(42 > 43)      # False

print('abcdf' > 'abcef')    # False
print('abc' > 'abcdef')     # False
print('abcdef' > 'abc')     # True
print('abc' > 'abc')        # False
print('abc' >= 'abc')       # True
print('abcdef' > 'abd')     # False
print('A' > 'a')            # False
print('Z' > 'a')            # False

print('3' > '24')           # True
print('24' > '3')           # False

# compare sets - determine if a set is superset or subset
print({3, 1, 2} < {2, 4, 3, 1})     # True
print({3, 1, 2} > {2, 4, 3, 1})     # False
print({2, 4, 3, 1} > {3, 1, 2})     # True

# lists (tuples) work similarly - compares each element in lexicographical manner
print([1, 2, 3] < [1, 2, 3, 4])     # True
print([1, 4, 3] < [1, 3, 3])        # False
print([1, 3, 3] < [1, 4, 3])        # True