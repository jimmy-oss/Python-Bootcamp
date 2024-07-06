#Dictionary
# dictionaries store collections of many
# many values of different types
# Unlike integers which start from o 
# dictionary indexes don't have to be integers
# but they can be strings, floats, booleans
# Indexes in dictionaries are called keys

# Creating empty dictionaries
my_dict = {}
my_dict = dict()
# Creating a dictionary with keys and values
my_cat = {'name':'Mr snuffles','age':5,'color':'grey'}
# In the above example we created a new dictionary
# that stores details about my_cat.
# We can fetch data from a dictionary by using our
# key as the index.

# Continuing from the above example let's say we want
# to print the name of my_cat,'Mr snuffles'
cat_name = my_cat['name']
print(cat_name) # Mr snuffles
# Unlike lists, dictionaries are unordered since the 
# indexing does not start at [0]
# We can also add items to a dictionary by defining a 
# new key and assigning it a value
birthdays = {"John":"August 1","Marcus":"April 8"}
birthdays["Mary"] = "September 14"
print(birthdays) # This prints {"John":"August 1","Marcus":"April 8"} etc
# Here we had a dictionary with the birthday of two people
# John and Marcus then we added Mary to our birthday dictionary
# We can also get the individual keys in the dictionary using the keys() method.

birthday = {"John":"August 1","Marcus":"April 8","Mary":"September 14"}
print(birthday.keys()) # this prints dict_keys(["John","Marcus","Mary"])
# The keys() method creates a dict_keys object that holds a list
# of all keys

# We can also convert them into a list using list() function
birthday = {"John": "August 1","Marcus":"April 8","Mary":"September 14"}
print(list(birthday.keys()))  # this prints ['John', 'Marcus', 'Mary']

# Setdefault() method