my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# 9. Given the above code, answer the following questions and explain your answers:
   
# Are the lists assigned to my_list and another_list equal?
# yes - both lists have the same values so the result will be equal

# Are the lists assigned to my_list and another_list the same object?
# no - they both have the same values but they are not referencing the same object

# Are the nested lists at index 3 of my_list and another_list equal?
# yes - they have the same values

# Are the nested lists at index 3 of my_list and another_list the same object?
# yes - when python duplicates a list, it performs what is known as a shallow copy. which means the nested elements are referencing the same object.

# Don't write any code for this exercise.