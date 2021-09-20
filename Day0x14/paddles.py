from turtle import Turtle, Screen

STARTING_POSITIONS = [(355, 0), (-355, 0)]
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.position_paddle(location)

    def position_paddle(self, where):
        if where == "right":
            self.goto(STARTING_POSITIONS[0])
        else:
            self.goto(STARTING_POSITIONS[1])

    def up(self):
        if self.ycor() <= 200:
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -200:
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)

    def auto_move(self):
        pass

