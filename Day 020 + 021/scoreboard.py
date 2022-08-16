from turtle import *

style = ('Courier', 20, 'italic')

class scoreboard(Turtle):
    def __init__(self):
        super(scoreboard, self).__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setposition(0, 265)
        self.write(f'Score: {self.score}', font=style, align='center')

    def incScore(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', font=style, align='center')

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', font=style, align='center')