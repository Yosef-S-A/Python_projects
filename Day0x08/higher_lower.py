#!/usr/bin/python3

import random
import art
from game_data import data
from os import system, name

score = 0

print(art.logo)


def clear_screen():
    # clear screen
    if name == 'nt':  # for Windows
        _ = system('cls')
    else:  # for linux and mac
        _ = system('clear')
    print(art.logo)


def set_result(list_a, list_b):
    '''function that compares number followers from game_data dictionary'''
    if (list_a['follower_count'] > list_b['follower_count']):
        result = 'a'
    if (list_a['follower_count'] < list_b['follower_count']):
        result = 'b'
    return result


def choose_person():
    '''function that randomly generates index for game_data list'''
    return random.randrange(len(data))


# Storing the indexes for later use in the question
comp_a = choose_person()

comp_b = choose_person()


def play():
    '''function that takes care of the game play'''
    global comp_a
    global comp_b
    global score

    print("Compare A: {}, {}, from {}.".format(
        data[comp_a]['name'], data[comp_a]['description'],
        data[comp_a]['country']))
    print(art.vs)
    print("Compare B: {}, {}, from {}.".format(
        data[comp_b]['name'], data[comp_b]['description'],
        data[comp_b]['country']))

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == set_result(data[comp_a], data[comp_b]):
        score += 1
        comp_a = comp_b
        comp_b = choose_person()
        clear_screen()
        play()
    else:
        print("Sorry, that's wrong. Final score: {}".format(score))


play()
