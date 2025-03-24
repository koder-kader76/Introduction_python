# string literals & dealing with quotes

greet = 'Hi there' # single quote
title = "Monty Python's Flying Circus" # double quotes

# Triple single quotes
king_arthur = '''
King Arthur: "What is your name?"
Black Knight: "None shall pass!"
King Arthur: "What is your quest?"
Black Knight: "I have no quarrel with you, but I must cross this bridge"
'''
print(king_arthur)

# Triple double quotes
talking_man = """
Man: "Is this the right room for an argument?"
Other Man: "I've told you once."
Man: "No you haven't
"""""
print(talking_man)

# str that needs double & single quotes
print('''My nickname is "Wolfy". What's yours?''')
print('My nickname is "Wolfy". What\'s yours?')
print("My nickname is \"Wolfy\". What's yours?")

# understanding backslash
# print("C:\Users\Xyyzy") # SyntaxError: (unicode error)
print("C:\\Users\\Xyyzy") # # Each \\ produces a literal \