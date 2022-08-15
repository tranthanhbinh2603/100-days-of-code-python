from turtle import *
from random import *

class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.color('blue')
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid=0.5)
        #Gọi 1 hàm khác
        self.refesh()
    def refesh(self):
        #self.hideturtle()
        self.goto(randint(0,280), randint(0,280))
        self.speed('fastest')

