from turtle import *
from random import *

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win this race? Enter a color: \n ("Blue", "DarkOrchid", "Red", "Black", "Green", "wheat", "Gray", "SeaGreen")')
position = [-80, -50, -20, 10, 40, 70, 100]
turtle = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]
colours = ["blue", "darkorchid", "red", "black", "green", "wheat", "gray", "seagreen"]
for i in range(0, 7):
    turtle[i].color(colours[i])
    turtle[i].shape("turtle")
    turtle[i].penup()
    turtle[i].goto(-230, position[i])

index = 0
winner = ''
while True:
    if (index == 7):
        index = 0
    if (turtle[index].xcor() >= 230):
        winner = colours[index]
        break
    turtle[index].forward(randint(1, 20))
    index += 1

if str(user_bet).lower() == winner:
    print(f"You've win. The winner turtle is {winner}.")
else:
    print(f"You've lose. The winner turtle is {winner}.")