#!/usr/bin/python3

import time
from turtle import Screen, Turtle
from score import Score
from paddles import Paddle
from ball import Ball

game_screen = Screen()
game_screen.setup(800, 600)
game_screen.bgcolor("green")
game_screen.register_shape("rectangle", ((5, -10), (-5, -10), (-5, 10), (5, 10)))
game_screen.tracer(0)

player1_score = Score()
player2_score = Score()
player1_score.create_score([-50, 255])
player2_score.create_score([50, 255])

ball = Ball()

player1_paddle = Paddle("right")
player2_paddle = Paddle("left")

game_screen.listen()
game_screen.onkey(player1_paddle.up, "Up")
game_screen.onkey(player1_paddle.down, "Down")
game_screen.onkey(player2_paddle.up, "w")
game_screen.onkey(player2_paddle.down, 's')


game_painter = Turtle()
game_painter.hideturtle()
game_painter.setpos(0, -295)
game_painter.seth(90)
game_painter.color("white")
game_painter.pensize(10)
game_painter.penup()
game_painter.shape("rectangle")

while game_painter.ycor() <= 300:
    game_painter.stamp()
    game_painter.forward(25)

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with the wall
    if ball.distance(player1_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        print("made contact")
    if ball.distance(player2_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect score()
    if ball.xcor() > 395:
        player1_score.set()
        ball.refresh()
        continue
    if ball.xcor() < -395:
        player2_score.set()
        ball.refresh()
        continue
    # detect collision to the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if player1_score.score == 2 or player2_score.score == 2:
        game_painter.home()
        game_painter.pencolor("Red")
        game_painter.write("GAME OVER", align='center', font= ("Times New Roman", 24, "bold"))
        game_is_on = False

game_screen.exitonclick()

