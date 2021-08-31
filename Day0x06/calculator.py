#!/usr/bin/env python3

from art import logo

print(logo)

def add(num1, num2):
	'''function that does addition'''
	return num1 + num2

def sub(num1, num2):
	'''function that does subtraction'''
	return num1 - num2

def mul(num1, num2):
	'''function that does multiplication'''
	return num1 * num2

def div(num1, num2):
	'''function that does division'''
	return num1 / num2

def calculator():
	''' This is a clculator function that can do claculations
	with the four basic arithmetic signs'''

	first_number = float(input("What's the first number?: "))
	
	op_list = ['+', '-', '*', '/']
	print("\n{}\n".format(op_list))
	
	cont_calc = 'y'

	while cont_calc == 'y':
		operation = input("Pick an operation: ")

		second_number = float(input ("What's the next number?: "))


		if (operation == "+"):
			result = add(first_number, second_number)
		elif (operation == "-"):
			result = sub(first_number, second_number)
		elif (operation == "*"):
			result = mul(first_number, second_number)
		elif (operation == "/"):
			result = div(first_number, second_number)

		print("{} {} {} = {}".format(first_number, operation, second_number, result))

		cont_calc = input ("Type 'y' to continue calculatin with {}, type 'n' to start a new calculation or 'e' to exit calculaiton: ".format(result))

		if cont_calc == 'y':
			first_number = result
			continue
		elif cont_calc == 'n':
			calculator()
		elif cont_calc == 'e':
			break

calculator()

print("Goodbye")
