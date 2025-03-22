# string literals can be continued over several lines
long_string = ("This is long string. "
               "It's actually very long. "
               "It spans multiple lines. "
               "Are you getting tired of this? "
               "So am i.")

long_string2 = """
    This is a long string.
    It's actually very long.
    It spans multiple lines.
    Are you getting tired of this?
    So am I.
"""

# list continuation
my_list = [
    "Antonina",
    "Brandi",
    "Trevor"
]

# Tuple continuation
my_tuple = (
    3.1415192,
    2.718282,
    1.414213,
)

# set continuation
my_set = {
    "Dog",
    "Cat",
    "Pet",
}

# use parentheses to delimit code
return (obj.bar1
      + obj.bar2
      + obj.bar3)

# use backslash to end any line you want to
# continue
result = value1 + \
         value2 + \
         value3 