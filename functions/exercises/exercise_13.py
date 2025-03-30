# 13. Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# ans: python will raise an error as the function's parameters has an default value in one and no default values in the subsequent parameters. In Python, if a parameter has a default value, then the following parameters must have a default value.

# SyntaxError: parameter without a default follows parameter with a default