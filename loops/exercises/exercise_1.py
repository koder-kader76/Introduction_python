# 1. The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)
    # counter += 1  # missing statement

# ans: the body of the while loop doesn't modify the counter - for all while loops, the body has to modify the counter element