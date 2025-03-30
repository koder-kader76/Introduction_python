# 10. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# ans:
# 42
# 3.141592
# 2

# python will take the first 2 arguments provided in the function invocation and print out 42 & 3.141592. As for the third argument, since none is provided, Python will use the default value provided in the parameter which is 2.