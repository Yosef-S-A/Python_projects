from turtle import Turtle

ALIGNMENT = "center"
FONT = "Times New Roman", 14, "bold"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.write("Score = " + str(self.score), False, align="center", font=("Times New Roman", 14, "bold"))
        self.hideturtle()
        self.penup()

    def set(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write("Score = " + str(self.score), False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

