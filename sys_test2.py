# Tip Calculator
# Create a program that lets the user input their total bill
# at a restaurant, and returns the total cost of the bill
# including a tip. Use 15% of the total bill as the
# tip calculation.

# For example, if the total bill is KSh 1000, 
# the tip is 0.15 * 1000 = KSh 150, so the total cost
# of the bill returned to the user is 1000 + 150 = KSh 1150.

# Once you're finished, take this a step further 
# and let the user enter their level of satisfaction
# with their service and factor that value into the 
# tip percentage. For example, if they received good service, the tip is 15%; great service is 20%; terrible service is 0%.

print("Welcome to njeri's Restaurant😊")
print("To continue please provide your total bill")

print("Chapati + Beans price") 
chapati = input()

print("Samosa price")
samosa = input()

print("Krest price")
krest = input()

print("You will receive your Total bill please rate our hospitality😊")
total = int(chapati) + int(samosa) + int(krest)

print("With all due of respect we give our customers freedom")
print("To express your Satisfactions based on our hospitality in njeri's Restaurant😊")
print("if our services is good😊, your tip is 15%")
print("if our services is great🌟, your tip is 20%")
print("if our services is terrible😔, your tip is 0%")

#total = float(input("Enter the total bill amount: "))
print("Your current bill is ksh: {total}")
print(total)
services = input("How was the service? (good, great, bad): ")

if services == "good":
    tip = 0.15 * total
elif services == "great":
    tip = 0.20 * total
else:
    tip = 0.00 * total

total_with_tip = total + tip
print("The total amount to pay is ksh: ", total_with_tip)
  
 
 