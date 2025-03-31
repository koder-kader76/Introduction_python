# 10. Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }

print(names)
# {'Nick', 'Max', 'Chris', 'Karl', 'Victor', 'Clare', 'Karis'}

# No - the names are stored in set which is an unordered collection and when python prints the values, it will be on a random order.

# to print the values in sorted order, you can use the sorted function which will print out a list
print(sorted(names))
# ['Chris', 'Clare', 'Karis', 'Karl', 'Max', 'Nick', 'Victor'