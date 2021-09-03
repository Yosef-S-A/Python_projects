#!/usr/bin/python3

import random
from art import logo

rand_num = random.randrange(1, 101)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def compare():
	'''function that checks if user input is correct or not'''
	global lives
	while lives != 0:
		print ("You have {} attempts remaining to guess the number".format(lives))
		guess = int(input("Make a guess: "))
		if (rand_num > guess):
			print("Too low")
		elif (rand_num < guess):
			print("Too high")
		else: 
			print("You got it! The answer was {}".format(rand_num))
			break
		lives -= 1
	else:
		print ("You've run out of guesses, you lose.")

def choose_level():
	'''function that sets the player turn based on the chosen game level'''
	global lives
	level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if level_choice == 'easy':
		lives = EASY_LEVEL_TURNS
	else:
		lives = HARD_LEVEL_TURNS

def play():
	'''function that activates game play'''
	#print("Psst, the correct anwer is {}".format(rand_num))
	choose_level()
	compare()

print (logo)

print ("Welcome to the Number Guessing Gmae!!")

print ("I'm thinking of a number between 1 and 100.")

play() 
