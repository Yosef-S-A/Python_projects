#!/usr/bin/python3

from turtle import Turtle, Screen
from random import randrange

screen = Screen()
screen.setup(width=800, height=800)


def position_turtles():
    x = -(screen.window_width() / 2 - 10)
    return x


y_pos = [100, 50, 0, -50, -100, -150]
color = ['green', 'yellow', 'red', 'blue', 'purple', 'orange']
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=position_turtles(), y=y_pos[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 380:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You win! The {} turtle is the winner.".format(winner))
                break
            else:
                print("You've lost! The {} turtle is the winner.".format(winner))
                break
        dist = randrange(50, 101)
        turtle.forward(dist)
