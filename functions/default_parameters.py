# default parameters

def say(text='hello'):
    print(text + '!')

say('Howdy')
say()

# default parameters
    # call a function without any arguments
    # once a default value has been assigned, all following parameters must have default parameters 

# def say2(msg1, msg2, msg3='dummy message', msg4):
#     pass
# SyntaxError: parameter without a default follows parameter with a default

# default values
    # can't accept the default value for parameter and provide an explicit value for following parameter

# e.g
def say3(msg1, msg2, msg3='dummy message', msg4='omitted mesage'):
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)

say3('a', 'b', 'c', 'd')
# a
# b
# c
# d

say3('a', 'b', 'c')
# a
# b
# c
# omitted message

say3('a', 'b')
# a
# b
# dummy message
# omitted message

say3('a', 'b', ,'d')
# a
# b
# d
# omitted message
# SyntaxError: invalid syntax (, ,'d')