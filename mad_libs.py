# Mad Libs application
# Create a mad libs kind of program that allows
# users to input word descriptions
# such as a "noun", a "verb", an "adjective" etc
# and create then display a funny story
# from the users input

print("Welcome to Jaw_Breaker_Application😂")
print("Before we proceed please enter your gender: male/female")
my_gender= input(str()).lower()

if my_gender == "male":
   print("welcome to men's conference😎")
   print("To continue as a man do you support valentines🤔")
   print("Yes😇, or No😈")
   man_quiz = input(str()).lower()
if man_quiz == "yes":
  print("Congratulation on your valentines day")
  print("I hope the chocolates you will eat will give you diarrhea")
  print("I hope you will not receive electricity at home ")
  print("I hope your car will breakdown on your way to work")
  print("I hope you will find a Tiger in your backyard")
elif man_quiz == "no":
  print("You are the goat of the day")
  print("You are a freedom fighter cheers to our holiday")
  print("You are the boss we shall drink and watch manchester united all day long")
elif my_gender != "man":
  print("You are a confused banger")
elif my_gender != "female":
  print("You are a confused banger")
elif my_gender == "female":
   print("What's up ladies remember what a man can do a women can do let's sing....😂 ")
   print("Welcome to Ladies Guys talk night")
   print("Before We continue do you have a boyfriend")
   print("Yes😈, or No😇")
   women_quiz = input(str()).lower()
   
if women_quiz == "yes":
  print("Wow your a naughty girl is he hot")
  print("I heard mary's boyfriend is a K-pop model") 
else:
 print("Your a confused banger")
  

