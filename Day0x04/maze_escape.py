#!/usr/bin/python3

# This program is written to solve the maze problem
# on Reeborg.ca (Reeborg's world) website

def turn_right():
	''' function defination to turn right the robot'''
    turn_left()
    turn_left()
    turn_left()

def complete():
	'''function that helps the robot navigate through the given maze'''
   if front_is_clear():
        move()
   elif right_is_clear():
        turn_right()
        move()
   elif wall_on_right() and front_is_clear():
        move()
   else:
        turn_left()

# loop that calls complete() function till success
while not(at_goal()):
    complete()
