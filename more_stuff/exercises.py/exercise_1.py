# 1. What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))    # CHRIS

# the function do_something takes a dictionary as an argument
# it will first return the dictionary view object - dictionary.keys() which will be sorted in ascending order
# ['Antonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor' ]
# after sorting, the index [1] of the dictionary.keys() - Chris
# The name 'Chris will be uppercase with .upper() method - 'CHRIS'