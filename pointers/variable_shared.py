##############################################
# variables & shared objects
##############################################

# Initialize numbers with a list
numbers = [1, 2, 3]

# assign a new variable to same list object
numbers2 = numbers

# numbers2 is a new variable - python will create a new variable on the stack
# both numbers1 & numbers2 point to the same object

print(id(numbers) == id(numbers2))
# True

print(numbers is numbers2)
# True

print(id(numbers))
# 4366530560
print(id(numbers2))
# 4366530560

# when numbers2 = numbers assignment takes place, Python does not copy the object, it copies the pointer to the object