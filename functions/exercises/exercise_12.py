# 12. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# ans: Python will raise an error as it is expecting at least 1 argument to be given during the function invocation but none is provided. So the program won't execute.

# TypeError: foo() missing 1 required positional argument: 'first'