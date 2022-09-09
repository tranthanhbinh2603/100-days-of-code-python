from turtle import *

class paddle(Turtle):
    def __init__(self, tuple):
        super(paddle, self).__init__()
        self.penup()
        self.color('white')
        self.setposition(tuple[0], tuple[1])
        self.shape('square')
        self.shapesize(4.5, 1.5)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
