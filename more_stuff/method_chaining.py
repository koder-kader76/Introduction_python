#  method chaining

# example of  code

tv_show = "Monty Python's Flying Cirus"
tv_show = tv_show.upper()
# "MONTY PYTHON'S FLYING CIRCUS"

tv_show = tv_show.split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']

# method chaining applies to methods instead of functions which will allow above code to be rewritten

tv_show = "Monty Python's Flying Cirus"
tv_show = tv_show.upper().split()
print(tv_show)
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRUS']


# no limit to chaining method calls but advisable to format code

letters = 'abcdefghijklmnopqrstuvwyz'
# Note that the parentheses surrounding this
# multi-line chain are required.
consonants = (letters.replace('a', '').
                      replace('e', '').
                      replace('i', '').
                      replace('o', '').
                      replace('u', ''))

print(consonants)
# bcdfghjklmnpqrstvwyz

# chaining in Python is not very common as most methods return None
# chaining can only be useful when all methods except the last return an object