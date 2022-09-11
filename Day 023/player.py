STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


from turtle import *

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape('turtle')
        self.color('Black')
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.FINISH_LINE_Y = 280

    def go(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)


