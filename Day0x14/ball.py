from turtle import Turtle
from random import choice

XY_MOVE = [10, -10]
SPEED = 0.05

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_speed = SPEED
        self.x_move = 0
        self.y_move = 0
        self.chose_move_dir()

    def chose_move_dir(self):
        self.x_move = choice(XY_MOVE)
        self.y_move = choice(XY_MOVE)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.home()
        self.move_speed = SPEED
        self.chose_move_dir()

