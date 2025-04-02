# 7. Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# create new list by splitting strings 
new_info = info.split(':')

# join the strings with '+' method
info = ('+').join(new_info)
print(info)

# Alternate solution

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info = info.replace(':', '+')
print(info)