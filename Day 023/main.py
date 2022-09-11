import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

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
        time.sleep(0.5)
        player.reset_turtle()

    time.sleep(0.1)
    screen.update()
