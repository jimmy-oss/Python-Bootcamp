# Mad Libs application
# Create a mad libs kind of program that allows
# users to input word descriptions
# such as a "noun", a "verb", an "adjective" etc
# and create then display a funny story
# from the users input

print("Welcome to Jaw_Breaker_Application😂")
print("Before we proceed please enter your gender: male/female")
my_gender = input(str()).lower()

if my_gender == "male":
   print("welcome to men's conference😎")
   print("To continue as a man do you support valentines🤔")
   print("Yes😇, or No😈")
   gender_quiz = input(str()).lower()
elif my_gender == "female":
   print("To continue as a lady do you support valentines🤔")
   print("Yes😇, or No😈")
   gender_quiz = input(str()).lower()

else:
  print("You are a confused banger")
  
  
if gender_quiz == "yes":
  print("Congratulation on your valentines day")
  print("I hope the chocolates you will eat will give you diarrhea")
  print("I hope you will not receive electricity at home ")
  print("I hope your car will breakdown on your way to work")
  print("I hope you will find a Tiger in your backyard")
elif gender_quiz == "no":
  print("You are the goat of the day")
  print("You are a freedom fighter cheers to our holiday")
  print("You are the boss we shall drink and watch manchester united all day long")
elif gender_quiz != "no":
     print("You are a confused banger")
elif gender_quiz != "yes":
  print("You are a confused banger")

else:
  print("You are a confused banger")
 

 
