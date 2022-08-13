from turtle import *

turtle = Turtle()
screen = Screen()

def forwards():
    turtle.forward(10)

def backward():
    turtle.backward(10)

def counter_clockwise():
    turtle.right(5)

def counter_clockwise():
    turtle.left(5)

def clockwise():
    turtle.left(-5)

def clear():
    turtle.setheading(0)
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkeypress(fun=forwards, key='w')
screen.onkeypress(fun=backward, key='s')
screen.onkeypress(fun=counter_clockwise, key='a')
screen.onkeypress(fun=clockwise, key='z')
screen.onkeypress(fun=clear, key='c')

screen.exitonclick()
