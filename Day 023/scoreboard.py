FONT = ("Courier", 24, "normal")

from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.setposition(-290, 260)
        self.write(f'LEVEL: {self.score}', font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f'LEVEL: {self.score}', font=FONT)

    def game_over(self):
        self.home()
        self.write(f'GAME OVER', align="center", font=FONT)

