import sys

name = sys.argv[1]
print("How old are you?")
age = int(input())

print(name)
print(age)

# Since sys.argv returns a list we used the sys.argv[1]
# This simply tells our application to pick the argument
# that is at index 1 in the list.
# the application is run and stores it as a variable name
 