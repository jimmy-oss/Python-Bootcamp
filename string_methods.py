# String Methods
# isalpha() = It returns True if the string
# consists of letters only and is not blank
# isalnum() = It returns True if the string
# consists of numbers and letters and is not blank
# isdecimal() = It returns True if the string contains
# only numeric characters
# isspace() = It returns True if the string contains
# only space,tabs or new lines
# istitle() = It returns True if the string contains
# words that start with uppercase letters
alpha = "Ilikeoldmusic"
password = "KJwertyuidf"
number_string = "123456"
tabbs = "    "
titles = "I Love Cups"
false_titles = "I love Cups"
print(alpha.isalpha())
print(password.isalnum())
print(number_string.isdecimal())
print(tabbs.isspace())
print(titles.istitle())
print(false_titles.istitle())
# The last print statement was false because not
# all words in false_titles were in uppercase
# These string methods are really useful when you
# want to do something like password validation
