# 6. What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# Ans: Nothing. The return keyword is executed before the print function call so python will tell the function to terminate the program and return whatever value is being invoked by the calling code which in this case is None.