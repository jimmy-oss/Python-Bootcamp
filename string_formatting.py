# String Formatting
# Way of embedding variables into strings
name = "James"
age = 19
print(f"My name is {name} and I am {age} years old")
# The f before the string stands for f-strings or
# formatted strings and allow us to put replacement fields
# {} with variable names inside our strings

# Raw Strings
# A raw string is a special type of string that allows us to 
# ignore all escape characters \ and print them out
print('Beyonce\'s lemonade stand')
# Here we use a proper escape \ character, by allowing us to add
# an apostrophe.But let us create a raw string and see what
# happens
print(r'Beyonce\'s lemonade stand')
# We notice the r before the string.This means raw string
# And in the output unlike the first example it prints out
# the escape character. 
