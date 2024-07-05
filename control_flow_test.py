# Magic 8 ball

#Create the popular Magic 8 Ball game.
# If you've never played it before, it is a toy
# that you can ask a yes-or-no question 
# and it will give you a random answer 
# feel free to read more on the Wikipedia page
#This is an external link.).
# In your program, allow a person to input a question,
# and then create a random number. 
# Based on the random number, 
# pick a response to the question 
# using if, elif, and else statements.
# You can find the responses at the Wikipedia page
#This is an external link..

print("Welcome to my Fortune-telling Shop😊")
print("To continue please feel free to ask any question....")
print("To continue choose Yes or No")
choice_one = "yes"
choice_two = "no"
if choice_two != "no" :
   print("Ohh sorry I guess your not ready for fortune telling😔")
elif choice_one == "yes":
   print("You chose yes ask what your question is?", input())
   print("...mmh wow my magic crystal has provided your lucky number that your seeking")
   print("Do you wish to continue remember with great fortune comes with a great responsibility")
   print(input())
elif choice_one == "yes":
  choice_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for i in choice_one:
    if i % 2 == 0:
      print("If you chose an even number your going to be wealthy", i)
      if i % 3 == 1:
        print("If you chose an odd number you are a hardworking person and you are so caring", i)

else:
  if choice_two != "no":
   print("Ohh sorry I guess your not ready for fortune telling😔")
 
  