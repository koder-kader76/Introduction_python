# 12. Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

# You should print True or False depending on each result.

# Solution 1:

# iterate through the numbers list & check if any of elements is equal to 3
def number_three(numbers):
    for number in numbers:
        if number == 3:
            return True
    
    return False

print(number_three(numbers1))   # True
print(number_three(numbers2))   # False
print(number_three(numbers3))   # False
print(number_three(numbers4))   # False
print(number_three(numbers5))   # True


# Solution 2:
# use the built-in function any keyword to check if any number is equal to 3

def number_three2(numbers):
    return (any([number == 3 for number in numbers]))

print(number_three2(numbers1))  # True
print(number_three2(numbers2))  # False
print(number_three2(numbers3))  # False
print(number_three2(numbers4))  # False
print(number_three2(numbers5))  # True

# ls:
print(3 in numbers1)          # True
print(3 in numbers2)          # False
print(3 in numbers3)          # False
print(3 in numbers4)          # False (3 != '3')
print(3 in numbers5)          # True  (3 == 3.0)