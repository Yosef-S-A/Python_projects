#!/usr/bin/env python3

from art2 import logo
from os import system, name

print(logo)

bidder_exist = "yes" #value to control the input loop

bid_ledger = {} #dictionary to store bids

#Welcome statement
print("Welcome to the Secret auction program.\n")

while (bidder_exist == "yes"):
    bidder_name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bid_ledger[bidder_name] = bid

    bidder_exist = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    #clear screen
    if name == 'nt': # for Windows
        _ = system('cls')
    else: # for linux and mac
        _ = system('clear')


max_bid = {} #dictionary to store the maximum bid(s)
bid_value = 0

# loop to identify the maximum value
for key in bid_ledger:
    if bid_ledger[key] > bid_value:
        bid_value = bid_ledger[key]
        max_bid = {}
        max_bid[key] = bid_ledger[key]
    elif bid_ledger[key] == bid_value:
        max_bid[key] = bid_ledger[key]

#check if there is a tie 
if len(max_bid) > 1:
    print("The following people have tied:")
    for key in max_bid:
        print(key)
    print("\n\n")
else:
    for key in max_bid:
        print("The winner is {} with a bid of ${}\n\n".format(key, max_bid[key]))
