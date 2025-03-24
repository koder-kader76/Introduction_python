# lists & tuples

my_list = [1, 'xyz', True, [2, 3, 4]]
print(my_list)

my_tup = ('xyz', [2, 3, 4], 1, True)
print(my_tup)

# e.g of multi-line format
monty_python = [
    # Begin multi-line list literal
    "Monty Python's Flying Circus",
    (
        # Begin multi-line tuple literal
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',
    ), # End multi-line tuple literal
] # End multi-line list literal


# Python weirdness
# to create a tuple with one element
one_tuple = (1)
print(type(one_tuple)) # <class 'int'>

two_tuple = (1,)
print(type(two_tuple)) # <class 'tuple'>