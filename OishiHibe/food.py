from turtle import Turtle
import random
from scoreboard import *


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("cyan")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.refresh()

  # Refreshes to a newer coordinate
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
