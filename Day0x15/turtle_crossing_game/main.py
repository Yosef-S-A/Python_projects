#!/usr/bin/python3

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from random import randrange
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
screen.listen()
screen.onkey(player_turtle.up, "Up")
screen.onkey(player_turtle.down, "Down")

car_manager = CarManager()
score = Scoreboard()
score.create_score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False

    if player_turtle.ycor() > 280:
        score.set()
        player_turtle.position_turtle()
        car_manager.level_up()
        
screen.exitonclick()

