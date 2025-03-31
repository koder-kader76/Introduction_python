# 2. Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# stuff is a tuple - tuples are immutable
# to change 'bye' to 'goodbye' - need to use list constructor to create a list from the tuple

stuffy_list = list(stuff)
print(stuffy_list)
# ['hello', 'world', 'bye', 'now']

# mutate the stuffy_list 
stuffy_list[2] = 'goodbye'
print(stuffy_list)
# ['hello', 'world', 'goodbye', 'now']

# re-assign stuff
stuff = tuple(stuffy_list)
print(stuff)
# ('hello', 'world', 'goodbye', 'now')