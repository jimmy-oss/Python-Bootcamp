# Magic 8 ball

# Create the popular Magic 8 Ball game.
# If you've never played it before, it is a toy
# that you can ask a yes-or-no question
# and it will give you a random answer
# feel free to read more on the Wikipedia page
# This is an external link.).
# In your program, allow a person to input a question,
# and then create a random number.
# Based on the random number,
# pick a response to the question
# using if, elif, and else statements.
# You can find the responses at the Wikipedia page
# This is an external link..

print("Welcome to my Fortune-telling Shop😊")
print("To continue please feel free to ask any question....")
print("To continue choose Yes or No")
user_choice = input().lower()

if user_choice != "yes":
    print("Ohh sorry I guess your not ready for fortune telling😔")
elif user_choice == "yes":
    print("You chose yes, ask what your question is?")
    input()
    print("...mmh wow my magic crystal has provided me your lucky number that you are seeking!")
    print("Do you wish to continue remember with great fortune comes with a great responsibilities")
    user_choice = input().lower()
    if user_choice == "yes":
        print("Type your lucky number")
        lucky_number = int(input())
        if lucky_number % 2 == 0:
            print("If you chose an even number that is " +
                  str(lucky_number) + " your going to be wealthy")
        else:
            print("If you chose an odd number that is " + str(lucky_number) +
                  " you are a hardworking person and you are so caring")
