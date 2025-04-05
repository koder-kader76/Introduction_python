# nested functions

def foo():
    def bar():
        print('BAR')
    
    bar()   # BAR

foo()
# bar()
# NameError: name 'bar' is not defined

# why need nested functions?

# encapsulation & organization

def calculate_total_price(items, tax_rate):
    def apply_tax(subtotal):
        return subtotal * (1 + tax_rate)

    subtotal = sum(item['price'] for item in items)

    return apply_tax(subtotal)

# data access without global variables

def process_data(data):
    processed_items = []

    def transform_item(item):
        # can access 'processed_items' from outer scope

        result = item * 2
        processed_items.append(result)
        return result
    
    for item in data:
        transform_item(item)
    
    return processed_items

# creating closures

def counter_factory():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

my_counter = counter_factory()
print(my_counter())     # 1
print(my_counter())     # 2

# code reuse within a limited scope

def analyze_text(text):
    def count_word(word):
        return text.lower().count(word.lower())
    
    result = {}
    result['python'] = count_word('python')
    result['code'] = count_word('code')
    result['function'] = count_word('function')

    return result

text = "Python is fun. I love coding in Python!"
print(analyze_text(text))

# callback functions

def process_list(items):
    results = []

    def callback(item):
        # can access the 'results' list
        processed = item.upper()
        results.append(processed)

    for item in items:
        callback(item)
    
    return results