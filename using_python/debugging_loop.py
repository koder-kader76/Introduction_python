# python

counter = 0
total = 0
numbers = [5, 10, 15, 20, 25]

for num in numbers:
    counter += 1
    total += num
    print(f"Iteration {counter}: added {num}, total is now {total}")

print(f"Final total: {total}")