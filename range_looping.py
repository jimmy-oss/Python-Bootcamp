# Range Looping
# The range() function returns a list
# for which we can use to loop through

list_a = list(range(0,5))
print(list_a)

# The range() function can take on two
# parameters.The first one is the number
# from where to start the range and the
# Second one is to stop the range
# This does not include that number
# In our example we start the range at o
# And end it at 5.Then we use the list()
# Method to convert it to a list and print it out

# Another use of range()
for i in range(0,7):
  print("I would love" + str(i) + "chapatis")
  
# In here we created a loop that prints out the string
# I would love chapatis with the number of chapatis
# incrementing with for loop.
# The str() method converts the number i to a string
# so that we could concatenate it with the rest of string
