# python

def convert_temperature(temp, unit):
    if unit == "C":
        # Convert Celsius to Fahrenheit
        converted = (temp * 9/5) + 32
        print('converted temp is', converted)
        return f"{temp}°C is {converted}°F"
    elif unit == "F":
        # Convert Fahrenheit to Celsius
        
        # original code with bug 
        # converted = temp - 32 * 5/9
        converted = (temp - 32) * 5/9
        print('converted temp is', converted)
        return f"{temp}°F is {converted}°C"
    else:
        return "Invalid unit. Use 'C' or 'F'"

# Test cases
print(convert_temperature(100, "C"))  # Should be 212°F
print(convert_temperature(32, "F"))   # Should be 0°C