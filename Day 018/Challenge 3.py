from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

tim.speed(1000)
for i in range(4, 10):
    degree = 360 / (i - 1)
    for z in range(1, i):
        tim.right(degree)
        tim.forward(100)


screen.exitonclick()