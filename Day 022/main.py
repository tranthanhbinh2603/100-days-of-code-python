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
from paddle import *


turtle = Turtle()
screen = Screen()

screen.bgcolor('black')
screen.setup(800,600)
screen.tracer(8)

l_paddle = paddle((350, 0))

screen.listen()
screen.onkey(fun=l_paddle.up, key='Up')
screen.onkey(fun=l_paddle.down, key='Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
