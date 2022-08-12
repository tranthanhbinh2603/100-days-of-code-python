from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

for _ in range(15):
    tim.forward(10)
    tim.penup() #Hàm đẩy bút lên
    tim.forward(10)
    tim.pendown()
screen.exitonclick()