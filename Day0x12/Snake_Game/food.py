from turtle import Turtle
import random

COLOR = ['DeepSkyBlue4', 'slateGray3', 'red3', 'aquamarine4']


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOR))
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.color(random.choice(COLOR))
        self.goto(random_x, random_y)

