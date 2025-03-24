# example of text sequence values
greet = "Hello"
respond = "He's pining for the fjords!"
year = '1969-07-20'

# text seq can be treated like ordinary seq
phrase = "there's no ketchup in this bottle"
for letter in phrase:
    print(letter)

# diff betweem ord seq & text seq
# ord seq contain zero or more objects
# characters in text sequences are not objects - just part of the value