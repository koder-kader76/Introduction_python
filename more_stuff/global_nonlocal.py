# the global and nonlocal statements

greeting = 'Salutations'

def well_howdy(who):
    # python will create a new variable
    # even if the variable exists in the outer
    # scope
    global greeting
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)


# when the global variable has not yet been defined 

def set_pi():
    global pi
    pi = 3.1415

set_pi()
print(pi)   # 3.1415


# nonlocal 

def outer():
   
    def inner1():
        
        def inner2():
            
            # global foo
            nonlocal foo
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")
        
        nonlocal foo
        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()
# print(f"global -> {foo} with id {id(foo)}")


# using global keyword

greet = "Salud"

def well_howdy(who):
    global greet
    greet = "Howdy!"
    print(f"{greet} {who}")

def well_hello(who):
    global greet
    greet = "Hello"
    print(f"{greet} {who}")

well_howdy('Angie')
well_hello('Angie')
print(greet)

# basic example

def counter():
    count = 0

    def increment():
        nonlocal count # this tells python we want to use the count variable from the outer function

        count += 1 # without local, this would create a new local variable

        return count
    
    return increment

# create a counter function
my_counter = counter()

# use the counter
print(my_counter())     # 1
print(my_counter())     # 2
print(my_counter())     # 3


# multiple nested functions example

def outer():
    x = 'outer'

    def middle():
        y = "middle"

        def inner():
            nonlocal x, y # access variables from both outer and middle functions
            x = "modified outer"
            y = "modified middle"
            print(f"Inside inner: x = {x}, y = {y}")
        
        inner()
        print(f"Inside middle: x = {x}, y = {y}")
    
    middle()
    print(f"Inside outer: x = {x}")

outer()
# Inside inner: x = modified outer, y = modified middle
# Inside middle: x = modified outer, y = modified middle
# Inside outer: x = modified outer


# example with multiple nested functions

def outer_function():
    x = "outer"

    def middle_function():
        nonlocal x
        x = "middle"

        def inner_function():
            nonlocal x
            x = "inner"
            print(f"Inner function: x = {x}")
        
        inner_function()
        print(f"Middle function: x = {x}")

    middle_function()
    print(f"Outer function: x = {x}")

outer_function()
# output:
# Inner function: x = inner
# Middle function: x = inner
# Outer function: x = inner


# Practical use case: a simple bank account

def create_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance
    
    def get_balance():
        return balance
    
    # return a dictionary of functions
    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "balance": get_balance,
    }

# create a new account
account = create_account(100)

# use the account
print(account["balance"]()) # 100
print(account["deposit"](50)) # 150
print(account["withdraw"](25))  # 125
print(account["withdraw"](200))  
# Insufficient funds
print(account["balance"]())