# Break Statement
# The break statement allows code to
# jump out a loop whenever a certain
# condition has been mer
number = 0
while True:
  print("I love candy" + " " + str(number))
  number +=1
  # is equal to number = number + 1
  if number == 7:
    break
  
# Each time the loop runs and prints out our statement,
# and checks if number is equal to 7.If not it runs 
# again until the loop stops
# This shorthand notation using compound assignment operators
# like += , -=, *=, /= etc. is commonly used in programming
# to make the code more concise and readable, especially when
# dealing with iterative operations like incrementing/decrementing 
# variables in loops.