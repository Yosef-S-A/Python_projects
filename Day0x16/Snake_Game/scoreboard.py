from turtle import Turtle

ALIGNMENT = "center"
FONT = "Times New Roman", 14, "bold"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as data:
            self.high_score = int(data.read())
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.write("Score = " + str(self.score) + " High Score = " + str(self.high_score), False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.penup()

    def set(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("Score = " + str(self.score) + " High Score = " + str(self.high_score), False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data", mode="w") as data:
                data.write("{}".format(self.high_score ))
        self.score = 0
        self.update_score()
