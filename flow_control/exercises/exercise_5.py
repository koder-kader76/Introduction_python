# 5. What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])       # Empty

# is_my_list is a function that evaluates the truthiness of the argument. during the function call, python will evaluate the empty list as falsy and thus will print from the else statement. if the list had contained any elements [0], it would have evaluated to truthy and the if block would have been executed