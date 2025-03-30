# 2. Take a look at this code snippet:

# What does this program print? Why?


foo = "bar"

def set_foo():
    foo = "qux"

set_foo()
print(foo)

# What does this program print? 
    # bar   
# Why?
    # foo was initialized outside the function scope and it was re-initialized again within the scope.

    # when set_foo() is invoked, there's no return value so python sets it to default None

    # after which print(foo) will look for the variable within its scope and will find "bar" and it will print "bar".