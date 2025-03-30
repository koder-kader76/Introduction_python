# Calling Functions

# invoking a function
def hello():
    print('Hello')
    return True

hello()     # invoking a function; ignore return value
prompt = hello()
# print('between the prompt & print')
print(prompt)  # using return value in a 'print' function call

# what does the print function return
print(print())          # None

# Functions can take one or more comma separated arguments
print('hello', 'goodbye', 'farewell')
# hello goodbye farewell

# you can spread them over multiple lines
print(
    'hello',
    'good-bye',
    'farewell',
    'adios',
    'ciao',
    'auf-wiedersehen',
)