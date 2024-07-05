#   Looping
# A loop is a way to execute some
# piece of code over and over again.

# For loops
# for loop is used when one wants to repeat 
# something a number of times

numbers = [1,2,3,4,5]

for number in numbers:
  print(number)
  
# The for statement loops through the numbers list,
# and stores each individual number in a variable
# called number.Then prints out which was created
# The variable number is used to hold each individual
# item from the numbers list during each iteration of
# the loop.
# The in keyword is used to specify the list(numbers) 
# that the loop will iterate over.
# The colon (: ) at the end of the line indicates
# the start of a new block of code that will be executed
# for each iteration of the loop.
# In the next line(s) of the code(not shown),
# there will be some operation(s) performed on the number
# variable, such as printing it or performing calculations
# with it.
# The important logic flow is that the loop will start 
# with the first item in the numbers list(1), 
# execute the code block with number set to 1, 
# then move to the next item(2), 
# execute the code block with number set to 2,
# and so on, until it has gone through all the items
# in the numbers list.
