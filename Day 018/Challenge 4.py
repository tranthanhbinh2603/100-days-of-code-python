from turtle import Turtle, Screen
from random import *
tim = Turtle()
screen = Screen()

#random walk
tim.speed(1000)
screen.colormode(255)
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
while True:
    tim.right(90 * randint(1, 4))
    #tim.color(choice(colours))
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    tim.pencolor(random_color)
    tim.forward(20)