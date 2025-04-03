# controlling loops

# 2 keywords can used to create more control over a program
# continue - to start a new loop iteration
# break - to terminate a loop

# continue

# example - you can use continue to skip over the loop when it meets a certain condition

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    # conditional expression
    # if name matches 'Max', continue will skip this expression and continue to the next loop
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)
# ['CHRIS', 'KARIS', 'VICTOR']
# upper_names does not contain 'Max'


# rewrite the prev program with a negated if loop

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    # use the negated if statement to skip
    # over 'Max'; continue not needed
    if name != 'Max':
        
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names)
# ['CHRIS', 'KARIS', 'VICTOR']

# continue is used to avoid code that becomes nested due to conditional logic

# e.g

# for value in collection:
#     if some_condition():
#         # some code here
#         if another_condition():
#             # some code here

# use continue to rewrite this loop

# for value in collection:
#     if not some_condition():
#         continue

#     # some code here

#     if not another_condition():
#         continue

#     # some more code here



#########################################
# breaking out of a loop
#########################################

# for instances where program is expected to quit when it meets a certain condition, the break keyword comes into play

# e.g - previously, the str.find() function searches for a substring - once it finds it, it returns the index where the substring is found, at that point where it finds the substring, it doesn't need to continue iterating through the text sequence. it can just a'break' it.

numbers = [3, 1, 5, 9, 2, 6, 4, 7]

found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        # add break when conditional expression is truthy
        # it will break the loop and stop any unnecessary iteration
        break

    index += 1

print(found_item)

# noted with nested loop
    # you can't break out of an outer loop if you are in a inner nested loop
    # same goes with continue



#########################################
# emulating do/while loops
#########################################

# example of a while loop

# while some condition is truthy
#     do some work

# a while statement only executes when condition is truthy - if condition is falsy it doesn't execute

# in some cases, the program may execute the loop at least once before terminating

# do some work
# while condition is truthy

# Python does not have a do/while or do/until loop

# use a break statement

# do some work
    # if some condition is falsy
        # break


# often needed in interactive programs where you may want to execute main program at least once

keep_going = True
while keep_going:
    # main loop code here

    answer = input('Play again? (y/n) ')
    if answer == 'n':
        keep_going = False

# a slightly more concise approach with a break statement

while True:
    # main loop code here

    answer = input('Play again? (y/n) ')
    if answer == 'n':
        break

