# python

def categorize_temperature(temp):
    print(f"Analyzing temperature: {temp}")
    
    if temp < 32:
        print("Temperature is below freezing")
        return "freezing"
    elif temp < 65:
        print("Temperature is cool")
        return "cool"
    elif temp < 85:
        print("Temperature is warm")
        return "warm"
    else:
        print("Temperature is hot")
        return "hot"

temps = [20, 45, 75, 90]
for temp in temps:
    result = categorize_temperature(temp)
    print(f"Result: {temp} is {result}")
    print("-" * 20)