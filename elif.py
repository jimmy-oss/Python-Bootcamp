# Elif
# What if we have more than one condition
# to check for? We can use the elif keyword
# to check for a multiple conditions 

height = 68 # inches
if height > 70 :
  print("You are really tall")
elif height > 60:
  print("Your height is average")
else:
  print("your really short")

# Since the height is greater than 60 the elif
# statement will be executed first and python 
# never reaches else but if our height was
# greater than 70 out python would never reach
# the elif statement and the else statement
# but if our height was lesser than 70 and 60
# our python would reach the else statement