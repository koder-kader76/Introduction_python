# sorting collections

# sorted - syntax: sorted(variable_name)
    # use sorted to create a sorted list from any collection
    # returns a sorted list from the elements in the collection
    # the original collection is unchanged

names = ('Grace', 'Clare', 'Allison', 'Trevor')
print(sorted(names))
# ['Allison', 'Clare', 'Grace', 'Trevor']
# the result is a list - not a tuple

print(names)
# ('Grace', 'Clare', 'Allison', 'Trevor')
# original tuple is unchanged

names = list(names)
print(names)
# ['Grace', 'Clare', 'Allison', 'Trevor']

print(names.sort())
# None
# returns none which implies the list has changed

print(names)
# ['Allison', 'Clare', 'Grace', 'Trevor']
# names list has been mutated by the method .sort()


# sorted & sort - by defult arrange elements in an ascending order
# you can change the order by adding a reverse=True keyword

names = [
    'Grace', 
    'Clare', 
    'Allison', 
    'Trevor',
]

print(sorted(names, reverse=True))
# ['Trevor', 'Grace', 'Clare', 'Allison']

names.sort(reverse=True)
print(names)
# ['Trevor', 'Grace', 'Clare', 'Allison']


# key=func 
    # pass key=function argument to tell sorted & sort how to arrange elements

words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))
# ['123', 'DEF', 'abc', 'xyz']

print(sorted(words, key=str.casefold))
# ['123', 'abc', 'DEF', 'xyz']

# sort list of numeric valued strings using key=int keyword argument

numbers = ['1', '5', '100', '15', '534', '53']
numbers.sort()
print(numbers)
# ['1', '100', '15', '5', '53', '534']

numbers.sort(key=int)
print(numbers)
# ['1', '5', '15', '53', '100', '534']