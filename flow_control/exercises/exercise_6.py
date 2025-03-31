# 6. Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def all_caps(message):
    # amend program to take input & character length
    entry = input("Enter a phrase: ")
    number = input("Enter the character limit: ")
    
    if entry:
        text = entry
    else:
        text = message
    
    if len(text) > int(number):
        return text.upper()
    else:
        return text
    

print(all_caps('john smith jones'))