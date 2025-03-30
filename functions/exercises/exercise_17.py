def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# 17. Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

# function names: say, line 1; used in line 7

# method names: .upper(), .lower(); used in line 7

# built-in functions: print (line 2); input (line 4, 5); max (line 7)