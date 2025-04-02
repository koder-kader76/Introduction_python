# splitting & joining strings

# str.split - returns a list of words in str; splits the string at sequences of one or more whitespace

text = '  Four      score and   seven years     ago. '
print(text.split())
# ['Four', 'score', 'and', 'seven', 'years', 'ago.']

print('no-spaces'.split())
# ['no-spaces']

# indicate the character python should split the string with as the argument
text = ',Four,score,and,,,seven,years,ago,'
print(text.split(','))
# ['', 'Four', 'score', 'and', '', '', 'seven', 'years', 'ago', '']

# str.split(' ') - specifying a delimiter changes the splitting behavior
    # looking for runs of whitespace, it splits the string at every occurrence of the delimiter
    # This also applies when using a literal space character as the delimiter

text = '  Four     score and   seven years ago.   '
print(text.split(' '))
# ['', '', 'Four', '', '', '', '', 'score', 'and', '', '', 'seven', 'years', 'ago.', '', '', '']

# str.split() - recognizes multi-character delimiters

text = 'Four<>score<:>and<>seven<>years<>ago'
print(text.split('<>'))
# ['Four', 'score<:>and', 'seven', 'years', 'ago']

# python doesn't allow using split to create lists or tuples

text = 'abcde'
# to create a sequence - use list/tuple constructor
print(list(text))
# ['a', 'b', 'c', 'd', 'e']
print(tuple(text))
# ('a', 'b', 'c', 'd', 'e')

# iterate strings a character at a time
text ='abcde'
for char in text:
    print(char)
# a
# b
# c
# d
# e

# str.splitlines - returns a list of lines from the string str
    # looks for line endings \n, \r, \n\r

text = '''
You were lucky to have a room. We used to have to
live in a corridor.
Oh we used to dream of livin' in a corridor!
Woulda' been a palace to us. We used to live in an
old water tank on a rubbish tip. We got woken up
every morning by having a load of rotting fish
dumped all over us.
'''

print(text.strip().splitlines())
#[
    # 'You were lucky to have a room. We used to have to', 
    # 'live in a corridor.', 
    # "Oh we used to dream of livin' in a corridor!", 
    # "Woulda' been a palace to us. We used to live in an", 
    # 'old water tank on a rubbish tip. We got woken up', 
    # 'every morning by having a load of rotting fish', 
    # 'dumped all over us.'
# ]


# str.join() - concatenates all strings in an iterable collection into a single lone string

words = ['You', 'were', 'lucky']
print(''.join(words))
# Youwerelucky
print(' '.join(words))
# You were lucky
print('\n '.join(words))
# You
#  were
#  lucky