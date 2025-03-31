# 8. How would you print all the numbers in the following range?

range(3, 17, 4)

# ranges are lazy sequences so python will not print the numbers until the program needs them
# so in this case, use the list constructor print out all the numbers in the range
print(list(range(3, 17, 4)))
# [3, 7, 11, 15]