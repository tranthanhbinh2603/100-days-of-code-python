import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import *
from random import *

class CarManager():
    def __init__(self):
        self.list_car = []

    def gen_car(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shapesize(stretch_wid=1, stretch_len=2)
        turtle.shape('square')
        turtle.color(choice(COLORS))
        turtle.goto(randint(320, 360), randint(-300, 300))
        self.list_car.append(turtle)

    def moving(self):
        for index in range(1, len(self.list_car) - 1):
            self.list_car[index].goto(self.list_car[index].xcor() - 10, self.list_car[index].ycor())


