##############################################
# equality & identity
##############################################

# two objects are equal
    # when obj1 == obj2 returns True

# the object is the same
    # when obj1 is obj2 returns True
    # aka obj1 & obj2 have the same identity

# Consider the following code:

# example 1:
numbers = [1, 2, 3]
numbers2 = numbers

print(numbers)
# [1, 2, 3]

print(numbers == numbers2)  # True
print(numbers is numbers2)  # True

# example 2:
my_list = [1, 2, 3]
my_list2 = [1, 2, 3]

print(my_list)
# [1, 2, 3]
print(my_list == my_list2)
# True
print(my_list is my_list2)
# False