import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.go, 'space')

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
loop_index = 0
while game_is_on:
    #Gen car
    car_manager.gen_car()
    car_manager.moving()
    # Khi con rua cham vao vung 280
    if player.ycor() >= player.FINISH_LINE_Y:
        scoreboard.add_score()
        SLEEP_TIME = SLEEP_TIME - (SLEEP_TIME * 50 / 100)
        time.sleep(0.5)
        player.reset_turtle()

    #Check xem rua co cham vao xe hay khong
    for car in car_manager.list_car:
        if player.distance(car) < 10:
            scoreboard.game_over()
            game_is_on = False

    time.sleep(SLEEP_TIME)
    screen.update()

screen.exitonclick()
