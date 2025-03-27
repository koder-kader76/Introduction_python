# 10. Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd'        # re-assignment
obj.upper()         # neither
obj = obj.lower()   # re-assignment
print(len(obj))     # neither
obj = list(obj)     # re-assignment
obj.pop()           # mutation
obj[2] = 'X'        # mutation
obj.sort()          # mutation
set(obj)            # neither
obj = tuple(obj)    # re-assignment     