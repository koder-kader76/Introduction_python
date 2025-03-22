# debuggin python using print example

# example of using print statement

max = '0'
for number in ['10', '2', '34', '6', '25']:
    # use print to debug code
    print('max =', max, 'number =', number,
          'number > max is', int(number) > int(max))
    if int(number) > int(max):
        max = number

print('max value is', max)