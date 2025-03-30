# 11. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)    # 42
    print(second)   # 3
    print(third)    # 2

foo(42)

# Ans: Python will take the first argument will print out to 42. Since the second and third arguments are not provided, python will take the default values provided in the parameters.