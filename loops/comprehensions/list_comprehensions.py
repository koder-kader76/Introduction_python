#############################################
# list comprehensions
#############################################

# comprehensions - to create a mutable collection from an existing iterable collection

# commone comprehensions - list comprehension

# [ expression for element in iterable if condition ]

# if condition - optional - tells Python to select only specific elements
# for element in iterable - describes the iteration - can be read as a for loop
# expression - value that gets returned by each iteration

#############################################
# transformations  
#############################################

# when an expression determines a new value based on an element from the original collection, it is known as a transformation - Hence the collections are known as transformations

# when the if condition is present, it is known as performing a selection - it is not unusual for original values to be returned through selection

# basic example of a transformative list comprehension

# iterating over the numbers 0 1 2 3 4
squares = [ number * number for number in range(5) ]
print(squares)
# [0, 1, 4, 9, 16]

# perform the same operation through a for loop
squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)
# [0, 1, 4, 9, 16]

# basic example of a selection

# iteration checking if number is divisible by 6
multiples_of_6 = [ number for 
                  number in range(20) 
                  if number % 6 == 0 ]
# for readability, you can separate lines

print(multiples_of_6)
# [0, 6, 12, 18]


#############################################
# example combining selection & trasformation
#############################################

even_squares = [ number * number 
                for number in range(10)
                if number % 2 == 0 ]

print(even_squares)
# [0, 4, 16, 36, 64]


# example of iterating over a dictionary

cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange'
}

names = [ name.upper() 
         for name in cats_colors ]

print(names)
# ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']

# this is identical to dictionary view objects
# also iterate over cats_colors.values() & cats_colors.items()


cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange'
}

# limit using selection for orange cats
names = [ name.upper() 
         for name in cats_colors 
         if cats_colors[name] == 'orange' ]

print(names)
# ['LEO', 'KAT']


# limit the selection to cats whose name starts with L
cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange'
}

# limit using selection for orange cats
names = [ name.upper() 
         for name in cats_colors 
         if name[0] == 'L' ]

print(names)
# ['LEO']


# get the values from the dictionary
cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange'
}

names = [ color 
         for color in cats_colors.values() ]

print(names)
# ['brown', 'orange', 'gray', 'black', 'orange']


# get the key, values from the dictionary
cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange'
}

# use tuple unpacking to retrieve key, value
names = [ f'{name}: {color}' 
         for name, color in 
         cats_colors.items() 
         if color == 'orange']

print(names)


# use multiple selection criteria in list comprehension
cats_colors = {
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange'
}

# multiple if statements act like nested if statements or and conditions
# the selections combine so only all matching criteria are selected
names = [ name.upper() 
         for name in cats_colors
         if cats_colors[name] == 'orange'
         if name[0] == 'L']

print(names)
# ['Leo']


# comprehensions also cn be used for multiple loop statements

# example of a deck of cards using comprehension

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Queen', 'King', 'Ace',]

deck = [ f'{rank} of {suit}'
        for suit in suits 
        for rank in ranks ]

print(deck)