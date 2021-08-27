#!/usr/bin/python3

# This project implements the rock-paper_scissors game
# The project is used to showcase the use of random module and list concept

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

usr_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
cmp_choice = random.randint(0,2)

print (choice[usr_choice])

print ("Computer chose:\n")
print (choice[cmp_choice])

if (usr_choice == 0 and cmp_choice == 2):
	print ("You win")
elif (usr_choice == 0 and cmp_choice == 1):
	print ("You lose")
elif (usr_choice == 1 and cmp_choice == 0):
	print ("You win")
elif (usr_choice == 1 and cmp_choice == 2):
	print ("You lose")
elif (usr_choice == 2 and cmp_choice == 0):
	print ("You lose")
elif (usr_choice == 2 and cmp_choice == 1):
	print ("You win")
else:
	print ("You tied")
