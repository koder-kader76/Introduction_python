############################################
# variables & objects
############################################

numbers = [1, 2, 3]

# 1. Python adds a new entry to the stack - assume its stack address is at 10240

# 2. Python allocates enough memory to hold the list and its elements on the heap - assume it allocates 32 bytes at address 4344278784

# 3. Python then constructs the list and its elements at address 4344278784

# 4. Last step, Python copies the address 4344278784 into the variable's stack address