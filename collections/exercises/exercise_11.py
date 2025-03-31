# 11. Consider the data in the following table:

# Name 	Country
# Alice 	USA
# Francois 	Canada
# Inti 	Peru
# Monika 	Germany
# Sanyu 	Uganda
# Yoshitaka 	Japan

# You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

# create a country dictionary which maps the names to their country of origin. Since names will always be unique, they have been placed as keys and the countries have been placed as values.

country = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan'
}

# test case to see if this data structure 
print(country['Alice'])     # USA
print(country['Inti'])      # Peru
print(country['Sanyu'])     # Uganda
