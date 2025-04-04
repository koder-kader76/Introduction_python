##############################################
# shallow vs deep copies
##############################################

# refer to below code example
# [[1, 2], 3, 4]

# when list object is created in the heap
    # nested list is not stored within the list
    # Python creates additional memory space for nested list
    # stores a pointer within the list to point to the nest list

# built-in constructors - create shallow copies when passed an element of the same type

my_list = [[1, 2], 3, 4]
shallow = list(my_list)
print(shallow[0] is my_list[0])
# True

my_dict = {'abc': [1, 2, 3]}
shallow = dict(my_dict)
print(shallow['abc'] is my_dict['abc'])
# True


##############################################
# shallow copies
##############################################

# shallow copy
    # duplicates the outermost level of object
    # nested objects are not duplicated - reference the same objects as the original

# example
import copy

# creates the list in heap; additional memory is created for the nested list
orig = [[1, 2], 3, 4]

# create a shallow copy of orig
dup = copy.copy(orig)

# orig & dup reference distinct objects
print(orig is dup)          # False

# orig & dup have the same values
print(orig == dup)          # True

# re-assigning orig element
orig[2] = 44

# dup is unchanged
print(dup)                  # [[1, 2], 3, 4]


# orig[0] & dup[0] reference the same object
print(orig[0] is dup[0])    # True

# re-assign the value in orif
orig[0][1] = 22

# orig & dup reference the same nested list which changes the dup 
print(dup)                  # [[1, 22], 3, 4]


##############################################
# deep copies
##############################################

# deep copy
    # exact duplicate of the original
        # including the nested levels
    # any changes to the original will not affect the duplicate

# revisit out earlier code

import copy

orig = [[1, 2], 3, 4]
dup = copy.deepcopy(orig)

print(orig is dup)      # False
print(orig == dup)      # True
orig[2] = 44
print(dup)              # [[1, 2], 3, 4]


# orig[0] & dup[0] are referencing two distinct objects
print(orig[0] is dup[0])    # False

# changes to orig[0] does not affect the dup nested list
orig[0][1] = 22
print(dup[0])           # [1, 2]


# copy.deepcopy
    # duplicates only mutable objects
    # if an object is iummutable - it references them


# shallow or deep copies?

# depends on mainly 3 things
    # on the data structure
    # whether your data has mutable content
    # whether it matters to your application

# best practices with shallow copies
    # working with objects that are not collections e.g integers, booleans
    # working with immutable objects with no mutable components
    # working with collections that have no mutable elements
    # performance - shallow copies are faster
    # if it doesn't matter if the mutable components are shared