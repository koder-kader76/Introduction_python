# 6. Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]


# solution 1: using a for loop and an if statement to check if the element is an even or odd number
even_odd = []

for number in my_list:
    if number % 2 == 0:
        even_odd.append('even')
    else:
        even_odd.append('odd')

print(even_odd)


# solution 2: using comprehensions to return a list with ternary expression

even_or_odd = [ 
    'even' if number % 2 == 0 else 'odd' 
    for number in my_list 
]

print(even_or_odd)

# ls solution:
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# define a function
def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

# call the function during comprehension
result = [ odd_or_even(number)
           for number in my_list ]
print(result)