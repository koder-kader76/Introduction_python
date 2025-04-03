# 7. Write a find_integers function that returns a list of all the integers from my_tuple:

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# 
# [1, 3, -4]

def find_integers(collection):
    result = [ element 
               for element in collection 
               if type(element) is int ]
    
    return result

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)
print(integers) 
