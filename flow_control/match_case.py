# match / case statement

# only introduced after 3.10

value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 nor 6')

# value is 5

# above statment is identical to an if statement

value = 5

if value == 5:
    print('value is 5')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')

# value is 5

# e.g match multiple values

value = 15

match value:
    case 11 | 12 | 13 | 14:
        print('value is < 15')
    case 15 | 16 | 17 | 18:
        print('value is >= 15')
    case _:
        print('value is neither < 15 or >= 15')