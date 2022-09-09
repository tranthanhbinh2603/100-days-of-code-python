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
import ball

from paddle import *
from ball import *
from time import *

turtle = Turtle()
screen = Screen()

screen.bgcolor('black')
screen.setup(800,600)
screen.tracer(8)

l_paddle = paddle((350, 0))
r_paddle = paddle((-350, 0))
ball1 = ball()

screen.listen()
screen.onkey(fun=l_paddle.up, key='Up')
screen.onkey(fun=l_paddle.down, key='Down')
screen.onkey(fun=r_paddle.up, key='w')
screen.onkey(fun=r_paddle.down, key='s')

game_is_on = True
while game_is_on:
    sleep(0.01)
    ball1.move()
    #Kiem tra neu no cham tuong
    if ball1.xcor() >= 280 or ball1.ycor() <= -280:
        ball1.bounce_x()

    # Cham vao tuong
    if ball1.distance(l_paddle) < 50 and ball1.xcor() > 350:
        ball1.bounce_y()

    #Mat bong
    if ball1.xcor() > 300:
        ball1.reset()
    if ball1.ycor() > 300:
        ball1.reset()

    update = screen.update()

screen.exitonclick()
