# logical operator precedence

# python has precedence rules for evaluating expressions with multiple operators & sub-expressions

# precedence from highest (top) to lowest (bottom)

# - ==, !=, <=, <, >, >= - Comparison
# - not - Logical NOT 
# - and - Logical AND
# - or - Logical OR

# e.g complex expressions that can be confusing 

print(1 or 2 and 3)     # 2 1
print(0 or 2 and 3)     # 2 3
print(1 or 0 and 3)     # 1 1
print(1 or 2 and 0)     # 1 1
print(0 or 0 and 3)     # 0 0
print(0 or 2 and 0)     # 0 0
print(1 or 0 and 0)     # 1 1
print(0 or 0 and 0)     # 0 0

print(1 and 2 or 3)     # 2 2
print(0 and 2 or 3)     # 3 3
print(1 and 0 or 3)     # 3 3
print(1 and 2 or 0)     # 2 2
print(0 and 0 or 3)     # 3 3
print(0 and 2 or 0)     # 0 0
print(1 and 0 or 0)     # 0 0
print(0 and 0 or 0)     # 0 0

# do not write code like above

# use parentheses to control how code gets written
# print((a and b) or (c and d))
# print(a and b or c and d)

# first line is easier to understand than second line

