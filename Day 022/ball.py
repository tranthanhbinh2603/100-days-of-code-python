from turtle import *
from math import *

class ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #print(f'{self.xcor()} {self.ycor()}')
        self.y_move *= -1

    def bounce_x(self):
        #print(f'{self.xcor()} {self.ycor()}')
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()