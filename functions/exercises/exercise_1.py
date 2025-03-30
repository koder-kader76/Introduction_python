# 1. What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# running program
# NameError: name 'foo' is not defined

# foo is a local variable which is defined within the function and cannot be accessed outside of the function
