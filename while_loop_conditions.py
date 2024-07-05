# While loops
# While loops run until certain condition
# is met.
players = 11
while players >= 5:
  print("The remaining players are",players)
  players -= 1
  
# A variable of players was created and set as 11
# And then we created a while loop with the condition
# that the value of players needs to be greater than
# or equal to 5.
# If this condition is true then a string will print
# and the value of players will decrease by 1
# and the loop will execute again until the condition
# is no longer true that is to say players is less than 5
# players -= 1: This line decrements the value of players by 1.
# In other words, it subtracts 1 from the current value of players
# and assigns the new value back to the players variable
# The purpose of this code is to repeatedly print the message
# "The remaining players are" along with the current value of players,
# while decrementing the value of players by 1 in each iteration of the 
# loop. This process continues until the value of players becomes less than 5,
# at which point the loop terminates.
