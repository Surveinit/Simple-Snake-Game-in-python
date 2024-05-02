from turtle import Turtle, Screen
import time

i = 0
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
#Directions
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0



class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("#f9f9f9")
        snake.speed(10)
        snake.goto(position)
        self.segment.append(snake)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
