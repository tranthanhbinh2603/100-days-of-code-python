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
        for i in position:
            # setup stake
            turtle = Turtle()
            turtle.penup()
            turtle.shape('square')
            turtle.color('white')
            turtle.goto(i)
            segment.append(turtle)
        self.head = segment[0]

    def move(self):
        for seg1 in range(len(segment) - 1, 0, -1):
            cor_x = segment[seg1 - 1].xcor()
            cor_y = segment[seg1 - 1].ycor()
            segment[seg1].goto(cor_x, cor_y)  # Lên 20 đơn vị
        segment[0].forward(moving_dis)

    def up(self):
        if segment[0].heading() != DOWN:
            segment[0].setheading(UP)

    def down(self):
        if segment[0].heading() != UP:
            segment[0].setheading(DOWN)

    def left(self):
        if segment[0].heading() != RIGHT:
            segment[0].setheading(LEFT)

    def right(self):
        if segment[0].heading() != LEFT:
            segment[0].setheading(RIGHT)