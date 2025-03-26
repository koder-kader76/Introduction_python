# 7. What will the following code do? Why?

# int('3.1415')

# Raises an error - string cannot be coerced into an integer as it is floating point number which requires float 

# correct coercion
print(float('3.141592'))


# ls solution
number = float('3.141592')
int_number = int(number)
print(int_number)