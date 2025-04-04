##############################################
# variables as pointers
##############################################

# x = 2
# looking at the above example
# x is the variable - 2 is the integer object assigned to it

# in this instance x points (references) integer object '2'

# python
    # all variables point to an object
    # if multiple variables are assigned to an object, they all point to (ref) to the same object
    # in essence they act like aliases for objects

# re-assignment
    # when you re-assign a variable, it doesn't alter the object that was previously reference
    # it changes which object the variable is pointing to
    # if the object doesn't exist, Python will create a new object
    # it will then change the variable's stack item to point to the new object

# mutable objects
# e.g 
# my_list = [1, 2, 3]
# my_list[1] = 4
# print(my_list) # [1, 4, 3]
    # if a variable points to a mutable object and you do something to the object, Python doesn't change the variable's stack item - it changes the variable
    # once a mutable object is changed, every variable that references that mutable object, it will now reference the object's new state


# numbers reference the list object
numbers = [1, 2, 3, 4]

# this is not re-assignment of numbers
# the list object is mutated
numbers[2] = 3333


# operations on variables
    # essential to remember some ops mutate objects & some don't
    # e.g list.sort mutates object
    # sorted(list) does not

# x is assigned to a list object
x = [1, 2, 3, 4, 5]
# x is re-assigned to a new list object
x = [1, 2, 3]
# the list object is mutated; x now references the list object's new state
x[2] = 4


# augmented assignment
    # when the variable on the left is assigned to an immutable object, the augmented assignment acts like re-assignment

# all the assignmens below are re-assignments
a = 42
b = 3.1415
c = 'abc'
d = (1, 2, 3)

a *= 2
b -= 1
b /= 3
c += 'def'
d += (4, 5)

# if the variable on the left references a mutable object, the augmented assignment is usually mutated

a = [1, 2, 3]
b = {'a', 'b', 'c'}

a += [4, 5]
a *= 2
b -= {'b'}

# all built-in types will be mutated when used as the target of an augmented assignment