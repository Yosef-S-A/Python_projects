#!/usr/bin/env python3

from art2 import logo
import random


print(logo)

card_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_value = {
    'A': [1, 11],
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}


def play():
    choice = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        global player_list
        global computer_list
        global player_score
        global computer_score

        player_list = []
        computer_list = []
        player_score = 0
        computer_score = 0

        player_list = [random.choice(card_deck), random.choice(card_deck)]
        computer_list = [random.choice(card_deck), random.choice(card_deck)]

        player_score = get_score(player_list, player_score)

        computer_score = get_score(computer_list, computer_score)

        game_play()

    elif choice == 'n':
        print("Goodbye")


def game_play():
    global player_list
    global computer_list
    global player_score
    global computer_score

    print("Your cards: {}, current score: {}".format(player_list, player_score))

    print("Computer's first card: {}".format(computer_list[0]))

    if (player_score > 21):
        print("Your final hand: {}, final score: {}".format(
            player_list, player_score))

        print("Computer's final hand: {}, final score: {}".format(
            computer_list, computer_score))
        print("Bust \n You Lose")
    elif (player_score < 21):
        player_choice = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if player_choice == 'n':
            while computer_score <= 16:
                computer_list.append(hit())
                computer_score = get_score(computer_list, computer_score)
            if computer_score <= 21:
                if computer_score > player_score:
		 print("Your final hand: {}, final score: {}".format(player_list, player_score))
		 print("Computer's final hand: {}, final score: {}".format(
		     computer_list, computer_score))
		 print("You Lose")
            	elif computer_score == player_score:
		 print("Your final hand: {}, final score: {}".format(player_list, player_score))
		 print("Computer's final hand: {}, final score: {}".format(
		     computer_list, computer_score))
		 print("Push \n It's a tie.")
		else:
		 print("Your final hand: {}, final score: {}".format(player_list, player_score))
		 print("Computer's final hand: {}, final score: {}".format(
		     computer_list, computer_score))
		 print("You win!!!")
	   else:
		print("Your final hand: {}, final score: {}".format(player_list, player_score))
		print("Computer's final hand: {}, final score: {}".format(computer_list, computer_score))
		print("You win!!!")

        elif player_choice == 'y':
            player_list.append(hit())
            player_score = get_score(player_list, player_score)
            game_play()

    else:
        print("You win!!!")


def hit():
    return random.choice(card_deck)


def get_score(sent_list, score):
    '''send score of cards'''
    if sent_list.__contains__('A'):
        for x in sent_list:
            if x == 'A' and (score + 11) < 21:
                score += card_value[x][1]
            elif x == 'A' and (score + 11) > 21:
                score += card_value[x][0]
            else:
                score += card_value[x]

    else:
        for x in sent_list:
            score += card_value[x]
    return score


play()
