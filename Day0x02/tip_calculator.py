#!/usr/bin/python3
""" This project is a simple terminal tip calculator.
 The project covers Data Types, Numbers, Operations, Type Conversions and f-Strings """

print("Welcome to the tip calculator.") #Welcome statement

#Accept values from user
# and cast the values into the appropriate data type
total = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? (10, 12, 15...)"))
people = int(input("How many people to split the bill?"))

#Calculate the tip
total_w_tip = total + (total * (percentage/100)) # calculate total value plus tip
pay_per_people = round(total_w_tip / people, 2) # divide equally amongests the grop

# print the pay per people
print("Each person should pay: ${} ".format(pay_per_people))
