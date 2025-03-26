# 2. This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# 1. One place is 6. 

# 2. Tens place is 3. 

# 3. Hundreds place is 9.

# 4. Thousands place is 4.

# Each digit may require multiple Python statements.

# 1 
one_place = 4936 % 10           # 6
print(one_place)

# 2 
tens_place = (4936 // 10) % 10  # 3
print(tens_place)

# 3
hundreds_place = (4936 // 100) % 10 # 9
print(hundreds_place)

# 4
thousands_place = 4936 // 1000      # 4
print(thousands_place)
