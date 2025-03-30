# 8. Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# Ans: Python will raise an error. foo function only takes 2 arguments but 3 are given. Too many arguments.