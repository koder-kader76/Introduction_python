# python

def process_user_data(user_dict):
    print(f"Starting with user data: {user_dict}")
    
    try:
        # Extract and process user information
        name = user_dict["name"]
        print(f"Found name: {name}")
        
        age = user_dict["age"]
        print(f"Found age: {age}")
        
        # Calculate some value
        birth_year = 2023 - age
        print(f"Calculated birth year: {birth_year}")
        
        return f"{name} was born around {birth_year}"
    except KeyError as e:
        print(f"Error: Missing key {e}")
        return "Incomplete data"

# Test with different data
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob"},  # Missing age
    {"age": 30}       # Missing name
]

for user in users:
    result = process_user_data(user)
    print(f"Result: {result}\n")