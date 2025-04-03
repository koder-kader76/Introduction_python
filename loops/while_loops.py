# while loops

#  a while loop - uses while keyword followed by a conditional expression, a colon (:) & a block

# why is while useful
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# rewrite this program with while loop

counter = 1
# python will evaluate the conditional expression
while counter <= 10:
    print(counter)
    # in a while loop; the block mus modify the counter
    counter += 1
    # not modifying the counter will cause an infinite loop - use ctrl-c 

# when the counter's value becomes 1001, the conditional expression will be falsy & the loop will break


# using while loops with sequences

# common use for while loops - to iterate over sequences and perform some action on each element

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']