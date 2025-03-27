# augmented assignment

# augmented assignment is shorthand for variable re-assignment

# e.g
foo = 42
foo = foo - 2
foo = foo * 3
foo = foo + 5
foo = foo // 25
foo = foo / 2
foo = foo**3
print(foo)              # 15.625

# using augmented notation for previous code
foo = 42
foo -= 2
foo *= 3
foo += 5
foo //= 25
foo /= 2
foo **= 3
foo %= 3
print(foo)              # 15.625

# augmented assignment with strings
bar = 'xyz'     # bar is 'xyz'
bar += 'abc'    # bar is 'xyzabc'
bar *= 2        # bar is 'xyzabcxyzabc'
print(bar)

# augmented assignment with lists
list_bar = [1, 2, 3]    # [1, 2, 3]
list_bar += [4, 5]      # [1, 2, 3, 4, 5]
print(list_bar)         # [1, 2, 3, 4, 5]

# augmented assignment with sets
set_bar = {1, 2, 3}     # {1, 2, 3}
set_bar |= {2, 3, 4, 5} # performs set union
                        # {1, 2, 3, 4, 5}
set_bar -= {2, 4}       # performs set difference
print(set_bar)          # {1, 3, 5}


# note: augmented assignment is a statement not an expression
# it can't be used as a function argument or return value

# def foo(bar):
#     print(bar)

# a = 3
# foo(a *= 2)

# syntaxerror: invalid syntax

# def foo():
#     a = 3
#     return(a *= 2)

# syntaxerror: invalid syntax