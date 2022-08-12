#Import thư viên cologram.py để lấy tất cả các màu trong bức tranh
# from colorgram import *
#
# rgb_color = []
# colors = extract('image.jpg', 100)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     turtle = (r, g, b)
#     rgb_color.append(turtle)
# print(rgb_color)

from turtle import *
from random import *
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
turtle = Turtle()
screen = Screen()
turtle.hideturtle()
turtle.speed(1000)
turtle.setheading(225)
turtle.penup()
turtle.forward(250)
turtle.setheading(0)
for z in range(1, 11):
    for i in range(1, 11):
        screen.colormode(255)
        turtle.pencolor(choice(color_list))
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)

    turtle.left(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


screen.exitonclick()