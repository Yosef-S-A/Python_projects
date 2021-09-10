#!/usr/bin/python3

import turtle as turtle_module
from random import randint

turtle_module.colormode(255)

tim = turtle_module.Turtle()
screen = turtle_module.Screen()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    for x in range(360 // size_of_gap):
        tim.speed(0)
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(150)


draw_spirograph(2)

screen.exitonclick()

