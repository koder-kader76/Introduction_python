# 5. On reflection, we've decided that we don't want to rely on using a global variable in the code we wrote in the previous example. To fix this, we're going to nest the code from the previous example into an outer function:

def all_actions():
    counter = 0

    def increment_counter():
        # global counter
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

# There's a bug in this code. Identify the bug, and fix it.

# Bug : NameError: name 'counter' is not defined

# when you use the global keyword for a variable, Python will place the variable in the global namespace

# the counter variable is inside a nested function increment_counter and to be able to access the variable in the all_actions() outer function, we use the nonlocal keyword