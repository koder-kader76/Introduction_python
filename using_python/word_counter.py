# python

# debugging problem

def count_words(sentence):
    words = sentence.split(" ")
    # use print to check word count
    print('words is', words)
    count = 0
    # use print to count 
    # print('count is', count)
    for word in words:
        count += 1
        # using print to count number
        print('count is', count)
    return count

test_sentence = "Python is fun to learn"
result = count_words(test_sentence)
print(f"The sentence has {result} words.")

mastery = "Launchschool is Mastery Based Learning"
m_result = count_words(mastery)
print(f"The sentence has {result} words.")