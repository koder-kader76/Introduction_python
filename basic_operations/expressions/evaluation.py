# expression evaluation

# python evaluates expressions from left to right (by default)

# e.g if operators are the same
total = 1 + 2 + 3 + 4 + 5   # 15

# e.g if operators are mixed
total = 4 * 5 - 1 + 2 * 3
# total = 20 - 1 + 6 # 25
# in the above example Python relies on precedence rules 

# use parentheses to explicitly tell python how to evaluate the expression

print(((4 * 5) - 1) + (2 * 3))          # 25
print((4 * ((5 - 1) + 2)) * 3)          # 72
print((((4 * 5) - 1) + 2) * 3)          # 63
print(4 * (5 - (1 + (2 * 3))))          # -8

# always use parentheses to tell python (and your users) how to execute your program