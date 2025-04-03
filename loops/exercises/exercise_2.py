# 2. Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.

# How old are you? 27

# You are 27 years old.
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# In 40 years, you will be 67 years old.

age = input('How old are you? ')
print(f'You are {age} years old.')

for number in range(10, 50, 10):
    print(f'In {number} years, you will be {int(age) + number} years old.')
