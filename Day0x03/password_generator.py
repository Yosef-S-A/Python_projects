#!/usr/bin/env python3

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

total_length = nr_letters + nr_symbols + nr_numbers
password = ""
pwd_list = []

for count in range(nr_letters):
	pwd_list += letters[random.randrange(0, len(letters))]
for count in range(nr_symbols):
	pwd_list += symbols[random.randrange(0, len(symbols))]
for count in range(nr_numbers):
	pwd_list += numbers[random.randrange(0, len(numbers))]

random.shuffle(pwd_list)

for count in range(total_length):
	password += pwd_list[count]

print("here is your password: {}".format(password))
