# Welcome message
print("test")
print("Welcome to bill calculator!")
# Input for Total Bill
totalBill = float(input("What was the total bill? $"))
# Input for the total pepople that are going to pay 
people = int(input("How many people to split the bill? $"))
#Input for the tip of your choice
tip = int(input("WHat percentage are you going to give? [10] [12] [15] "))
# Tip system to charge according to the tip of your choose
if(tip == 10):
    tipMath = totalBill * 0.1 
elif(tip == 12):
    tipMath = totalBill * 0.12
elif(tip == 15):
    tipMath = totalBill * 0.15
# Final math
finalBill = totalBill + tipMath
yourPart = finalBill / people
# Final print message with the value you should pay with a concatenation element
print("Each person should pay: " + str(yourPart))