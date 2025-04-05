# function definition order

# example
# top()
# NameError: name 'top' is not defined

def top():
    bottom()

def bottom():
    print('Reached the bottom')

top()

# rule of thumb: define all function definitions before invoking them