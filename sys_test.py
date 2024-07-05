# Birthday dates
#Create a program where you prompt a user for their
# age and return the year they were born.
#After that, return the year they will turn 81.

print("Which year is your birthday?")
year = input()
print(year)

print("How old are you actually?")
age = input()
print(age)

print("Great this means you will turn 81 on!")
subtract = 2080
subtract = subtract - int(year)
print(subtract)
