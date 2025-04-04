set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# 2. Without running this code, what will it print? Why?

# Don't worry about having an exact match for the output. The important part is to show something that accurately represents set2.

# output:
# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

# on line2 when set1 is assigned to set2, these 2 variables now reference the same object.

# when a variable is assigned to another variable, Python does not copy the object. It copies the pointer ans places it in the variables stack item.

# when set1's value is mutated, set2 will show the object's new state when the print function is invoked