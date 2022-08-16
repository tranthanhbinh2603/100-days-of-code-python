# 7 bước làm nên game stake:
# 1. Tạo ra body rắn
# 2. Di chuyển rắn - Làm cho rắn di chuyển được
# 3. Điều khiển được rắn
# 4. Sự kiện khi rắn chạm vào thức ăn
# 5. Tạo ra bảng điểm
# 6. Sự kiện khi rắn chạm vào tường
# 7. Sự kiện rẵn chạm vào chính nó

from stake_class import *
from food import *
from scoreboard import *
from math import *

screen = Screen()
screen.title('Trò chơi rắn - Stake game')
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0) #Tắt cập nhật màn hình và tắt cả hoạt ảnh rùa

snake = Snake()

#Bắt sự kiện nhấn nút:
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

food = Food()
score = scoreboard()

game_is_on = True
while game_is_on:
    #Code để update màn hình
    screen.update()
    sleep(0.05)
    #Di chuyển rắn
    # for seg in segment:
    #     seg.forward(20)
    snake.move()

    #Chạm vào thức ăn
    if (snake.head.distance(food) < 15):
        food.refesh()
        score.incScore()
        snake.exten_snake()

    #Chạm vào tường:
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        score.game_over()

    #Chạm vào rắn

screen.exitonclick()