# re-assignment vs mutation

# 2 ways to alter values in python
    # re-assignment - change the binding of the variable to reference a different obj

    # mutation - change the value of the obj the variable is referencing

num =  3    # assignment(initialization)
my_list = [1, 2, 3] # assignment(initialization)
my_dict = {
    'a': 1,
    'b': 2,
}           # assignment(initialization)

num = 42    # re-assignment
my_list[1] = 42     # re-assignment of elem
                    # my_list is mutated
my_dict['b'] = 3    # re-assignment of elem
                    # my_dict is mutated

# you can still re-assign the variables
my_list = [2, 3, 4]     # re-assignment
my_dict = { 'x': 0 }    # re-assignment