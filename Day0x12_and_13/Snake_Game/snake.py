from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for block in STARTING_POSITIONS:
            self.add_segment(block)

    def add_segment(self, position):
        new_part = Turtle(shape='square')
        new_part.color('magenta')
        new_part.penup()
        new_part.goto(position)
        self.segments.append(new_part)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            num_x = self.segments[seg_num - 1].xcor()
            num_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(num_x, num_y)
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

