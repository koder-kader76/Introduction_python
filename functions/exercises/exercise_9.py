# 9. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# ans
# 42
# 3.141592
# 2.718

# even though the parameters have default values, python will take the value of the arguments