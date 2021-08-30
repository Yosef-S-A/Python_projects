#!/usr/bin/python3

import random
from hangman_art import *
from hangman_word import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# A variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You've already guessed {}".format(guess))
        print("{}".format(' '.join(display)))
        continue

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print("You guessed {}, that's not in the word. You lose a life.".format(guess))
        print(stages[lives])
        lives -= 1
    if lives == 0:
        print("You Lose")
        print(stages[lives])
        print("The word was {}".format(chosen_word))
        end_of_game = True
    # Join all the elements in the list and turn it into a String.
    print("{}".format(' '.join(display)))

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
