# 7. What happens when you run the following code?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon ' + NAME)
print('Good Evening, ' + NAME)

# following code will print 
# Good Morning, Victor
# Good Afternoon, Victor
# Good Evening, Victor

# Good Morning, Nina
# Good Afternoon, Nina
# Good Evening, Nina

# Why - the first line initializes the variable NAME to Victor. Python creates a space in memory for the value of 'Victor' and allocates a small space for NAME variable and stores the value's address in the variable's address. 

# When the variable is called in the next few lines, python checks the variables address in the memory and retrieves the address in which 'Victor' is stored. Python then proceeds to extract the value from the address and prints it out to screen.

# in the following line, the NAME is now re-assigned to 'Nina'. Python does the same thing, it allocates a memory space to hold 'Nina' and stores the value's address in variables memory, replacing the previous value of 'Victor's address.

# so the first part is initialization & the second part is re-assignment. To take note the NAME variable is in uppercase which represents a constant in python and it is the wrong idiomatic expression to use. the correct expression would be to use 'name' variable in lower_case.