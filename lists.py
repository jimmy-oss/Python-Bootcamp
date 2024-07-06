# Lists
# A python3 list can store any kind of value
# We create a list using square brackets [] or
# using the list() function like this
# my_list = []
# my_other_list = list()

list_a = ["a","b","c","d"] # list of strings
list_b = [1,2,3,4,5,5] # list of numbers
list_c = [1,"west",32,"flowers"] # mixed list

# We can create a list that holds similar types of
# items,such as the first two which hold only strings
# or only numbers or we can mix the types of data
# stored in our list as we do with list_c which
# holds both numbers and strings

# Nest our lists with other lists
list_d = [["a","b","c","d",[1,2,3,4,5,6],[1,"west",4,"today"]]]
# nested list

# We can join two lists using the extend() method
list_a = ["a","b","c","d"]
list_b = [1,2,3,4,5,6]
# Joining list_b to list_a
list_a.extend(list_b)
print(list_a) # This will print ["a","b","c","d",1,2,3,4,5,6]
print(list_b)# This will print [1,2,3,4,5,6]
# Here we have joined list_b to list_a
# This adds new values to list_a and list_b remains unchanged

# We can also use the append() method
list_a = ["a","b","c","d"]
print(list_a)  # ["a","b","c","d"]
list_a.append("e")
print(list_a)  # ["a","b","c","d","e"]

# Here we append a single value "e" to the list.

# We can also arrange list items in place using
# the reverse() and sort() methods
list_a = ["a","b","c","d"]
list_a.reverse()
print(list_a) # ["d","c","b","a"]
# Here we use the reverse () method to reverse the list

# Sort method
list_a = [1,3,4,5,6,2]
list_a.sort()
print(list_a) # [1,2,3,4,5,6]
# The sort() method arranges items in an orderly mannner

# Another note is that reverse and sort methods only work
# on the list they were called on.They have no return value
list_a = [1,2,3,4,5,6]
list_a.reverse() # converts list_a to [6,5,4,3,2,1]
# list_b = list_a.reverse() # list_b is none you will get an error
