#procedural programing

#How to use OOP
from turtle import Turtle, Screen
import random
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
for i in range(1,361):
    timmy.forward(40)
    timmy.left(i)
# for i in range(1,361):
#     timmy.forward(30)
#     timmy.right(i)
# while True:
#     long = random.randint(1, 30)
#     degree = random.randint(1, 180)
#     timmy.forward(long)
#     timmy.left(degree)


my_screen = Screen()
print(my_screen.canvwidth) #Attribute
my_screen.exitonclick() #method

#Ex 2:
##install package: pip install PrettyTable
##Or File -> Setting -> Project... -> Python Interpreter -> Dấu cộng -> Gọi thư viện lên cài.
# from prettytable import PrettyTable
# #right click -> Go To -> Implentient
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

