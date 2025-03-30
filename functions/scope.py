# scope

# scope of an identifier determines where you can use it

# e.g

def well_howdy(who):
    greeting = "Howdy"
    print(f"{greeting}, {who}")

well_howdy("Angie")
# Howdy, Angie
# print(greeting)
# NameError: name 'greeting' is not defined

greeting2 = 'Salutations'

def well_howdy2(who2):
    greeting2 = 'Howdy'
    print(f'{greeting2}, {who2}')

well_howdy2("Angie")
# Howdy, Angie
print(greeting2)
# Salutations

# variable shadowing 
    # assignment on line 19 hides the variable assignment from line 16

# remove assignment in function
greeting3 = 'Salutations'

def well_howdy3(who3):
    print(f'{greeting3}, {who3}')

well_howdy3('Angie')
# Salutations, Angie
print(greeting3)
# Salutations

# if there are no assignments in the function body, python will look for the variable assignment in the lexical scope - outerscope 

def scope_test():
    if True:
        foo = 'Hello'
    else:
        bar = 'Goodbye'
    
    print(foo)
    # print(bar)

scope_test()
# Hello
# UnboundLocalError: cannot access local variable 'bar' where it is not associated with a value

# in the above example - both variables are technically in scope but since else statement never runs, bar is never assigned
# thus the UnboundLocalError

