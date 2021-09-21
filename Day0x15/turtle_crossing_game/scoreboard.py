from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

    def create_score(self):
        self.penup()
        self.goto(-280, 255)
        self.write("Level: "+str(self.level), False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.penup()

    def set(self):
        self.level += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write("Level: "+str(self.level), False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

