# python

def titlize(sentence):
    words = sentence.split()
    new_words = []
    
    # Add print statements to inspect variables
    print(f"Original words: {words}")
    
    for word in words:
        if len(word) > 2:
            # Bug is here: capitalize() doesn't modify the string in-place
            word.capitalize()
            print(f"After capitalize attempt: {word}")
            new_words.append(word)
    
    print(f"Final new_words: {new_words}")
    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))