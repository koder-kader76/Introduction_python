# conditionals

# e.g of if conditional
value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

# e.g of if conditonal with elif
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')


# if statements may contain multiple lines
if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    print('value is 9')
    print('value is an odd number')
    print('value is NOT a prime number')
else:
    print('value is something else')


# if statement that does nothing - use pass
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass    # We don't care about 9
else:
    print('value is something else')

# adding a comment to a pass is good practice