# 7. Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# Ans: Python will raise an error; foo function takes 2 parameters but only 1 argument is given when the function is called

# TypeError: foo() missing 1 required positional argument: 'qux'
