# 5. Print all of the even numbers in the following list of nested lists. Don't use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for number in my_list:
    for even in number:
        if even % 2 == 0:
            print(even)

# using comprehension to print out a list of even numbers in nested loops
numbers = [ even_number
            for number in my_list
            for even_number in number 
            if even_number % 2 == 0 ]

print(numbers)