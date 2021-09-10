#!/usr/bin/python3

import turtle as turtle_module
import random



def draw_spirograph(size_of_gap):
    for x in range(360 // size_of_gap):
        tim.speed(0)
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(150)

draw_spirograph(2)
