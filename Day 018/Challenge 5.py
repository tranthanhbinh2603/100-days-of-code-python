from turtle import Turtle, Screen
from random import *
tim = Turtle()
screen = Screen()

#random walk
tim.speed(1000)
screen.colormode(255)
for i in range(1, 37):
    tim.circle(50)
    tim.right(10)
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

screen.exitonclick()
