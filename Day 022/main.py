# Các thành phần của game Pong: (Break the problem)
# - Theo mình: Làm 2 tấm ván - Làm nền vạch -  Làm bảng điểm - Làm event chạm vào 2 tấm ván và mất bóng
#
# - Đáp án:
# 1. Tạo ra màn hình
# 2. Tạo ra và di chuyển tấm ván
# 3. Tạo ra tấm ván thứ 2
# 4. Tạo ra quả bóng và làm cho nó di chuyển
# 5. Sự kiện khi chạm vào tường (tung lên)
# 6. Sự kiện khi chạm vào ván
# 7. Sự kiện khi mất bóng
# 8. Tạo bảng điểm

from turtle import *


turtle = Turtle()
screen = Screen()




screen.bgcolor('black')
screen.setup(800,600)

turtle.hideturtle()
turtle.color('white')
turtle.penup()
turtle.setposition(350, 0)
turtle.shape('square')
turtle.shapesize(4.5, 1.5)
turtle.showturtle()

def up():
    turtle.setheading(90)
    turtle.left(100)

screen.listen()
screen.onkey(fun=up, key='Up')

screen.exitonclick()
