# code blocks
if is_ok():
    print('first thing')
    print('another thing')
    print('yet another thing')
print('This is not part of the above block')

if is_something():
    print('do something')
    print('do another thing')
else:
    print('do something else')

while try_again():
    print('first thing')
    print('another thing')
    print('yet another thing')
print('The loop has ended')


# you can have multiple levels of indentation
# but recommended not more than 2

if value <= 10:
    print('value <= 10')
    if value >= 5:
        print('value >= 5')
    else:
        print('value <= 5')
else:
    print('value > 10')