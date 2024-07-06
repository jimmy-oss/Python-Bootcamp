# Continue Statement
# The continue statement is also
# used in loops.It allows us to
# jump back up to the top of our loop
# The continue keyword ignores all other statements
# under it and they are not run

'''In a team of members is 20 some numbers
are taken and want to display the numbers 
that are not taken so others don't pick
the picked numbers'''

# Taken numbers
numTaken = [3,5,7,11,13]
print("Available numbers")
# Loop
for i in range(1,21):
  if i in numTaken:
    continue
  print(i)

# We want to print numbers from 1-20 but skip
# over the numbers in the numtaken list
# for loop takes place if the current number i
# is in the numTaken list the print() statement directly
# under the continue is not executed.This is because
# every time continue is called,Python3 jumps back up to 
# the top of the loop