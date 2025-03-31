# 2. Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

print(even_or_odd(10))
print(even_or_odd(3))
print(even_or_odd(9))
print(even_or_odd(4))
print(even_or_odd(22))
print(even_or_odd(8))


# e.g using ternary operator

def even_or_odd2(num):
    return ('even' if num % 2 == 0 else 'odd')

even_or_odd2(10)
even_or_odd2(3)
even_or_odd2(9)
even_or_odd2(4)
even_or_odd2(22)
even_or_odd2(8)


# same program as above but getting an input from user

def even_odd():
    number = input("Enter a number: ")
    if number.isdigit():
        if int(number) % 2 == 0:
            print('even')
        else:
            print('odd')
    else:
        print("Please enter a valid number")

even_odd()