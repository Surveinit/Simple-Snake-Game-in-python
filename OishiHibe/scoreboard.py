from turtle import Turtle, Screen
import time

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_int = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)       # move to top center of screen
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, 240)
        self.write(f"Score: {self.score_int}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.color("white")
        self.write(f"Score: {self.score_int}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_int += 1
        self.clear()
        self.update_scoreboard()
