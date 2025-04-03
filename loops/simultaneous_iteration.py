#############################################
# simultaneous iteration
#############################################

# simultaneous iteration - some programs may require iterating through more than 1 collection at a time

# initial way of collecting data from multiple collections is using a while loop

########################
# example of while loop
#########################

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0
while index < len(forenames):
    # surnames may be shorter
    if index >= len(surnames):
        break

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1

# Ken Camp
# Lynn Blake
# Pat Flanagan
# Nancy Short

#############################################
# using zip
#############################################

# while the above example proves to be effective, it is also error-prone

# alternative would be to use zip
# zipped_iterables = zip(collection1, collection2, ....)

# example of above code with zip

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

# returns a lazy sequence iterable
full_names = zip(forenames, surnames)

# use tuple unpacking to print out names
for forename, surname in full_names:
    print(f'{forename} {surname}')

# Ken Camp
# Lynn Blake
# Pat Flanagan
# Nancy Short

# zip also takes care of the problem of collections being shorter - it assumes the collection that is shortest and terminates the loop