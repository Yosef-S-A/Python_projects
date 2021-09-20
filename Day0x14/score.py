from turtle import Turtle

ALIGNMENT = "center"
FONT = "console", 24, "bold"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def create_score(self, position):
        self.color("white")
        self.penup()
        self.goto(position[0], position[1])
        self.write(str(self.score), False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.penup()

    def set(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(str(self.score), False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

