from turtle import *
from time import *

moving_dis = 20
position = ([-40, 0], [-20, 0], [0, 0])
segment = []

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        for i in position:
            # setup stake
            self.add_segment(i)
        self.head = self.segments[0]

    def move(self):
        for seg1 in range(len(self.segments) - 1, 0, -1):
            cor_x = self.segments[seg1 - 1].xcor()
            cor_y = self.segments[seg1 - 1].ycor()
            self.segments[seg1].goto(cor_x, cor_y)  # Lên 20 đơn vị
        self.segments[0].forward(moving_dis)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def add_segment(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.speed(10)
        turtle.shape('square')
        turtle.color('white')
        turtle.goto(position)
        self.segments.append(turtle)

    def exten_snake(self):
        self.add_segment(position[-1])