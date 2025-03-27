# 3. Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.

person_age = input("How old are you? ")

age = int(person_age)
print(f"You are {age} years old.")

years = list(range(10, 50, 10))

for i in years:
    print(f"In {i} years, you will be {age + i} years old.")