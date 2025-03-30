# mutating the caller

# some methods mutate the object it is called upon
# e.g

odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop()
print(odd_numbers)  # [1, 3, 5, 7]

# some functions mutate their arguments
# e.g.

def add_new_number(my_list):
    my_list.append(9)

numbers = [1, 2, 3, 4, 5]
add_new_number(numbers)
print(numbers)      # [1, 2, 3, 4, 5, 9]


# mutating caller is acceptable but mutating arguments is bad practice

def add_new_number(my_list):
    return my_list + [9]

numbers = [1, 2, 3, 4, 5]
new_numbers = add_new_number(numbers)
print(new_numbers)      # [1, 2, 3, 4, 5, 9]
print(numbers)          # [1, 2, 3, 4, 5]

# debug method's code or check documentation to check if method mutates caller if caller is mutable