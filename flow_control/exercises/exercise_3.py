# 3. Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found')

bar_code_scanner('113')     # Product2
bar_code_scanner(142)       # Product not found

# match/case statement compares the argument to the values provided.

# the first invocation matches the data type and the value, so it prints Product2

# the second invocation does not match the data type as the case statement is expecting a string but the argument provided is a integer