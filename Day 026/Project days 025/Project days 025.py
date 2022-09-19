#https://www.sporcle.com/games/g/states
import random
from turtle import *

#import pandas
from pandas import *

screen1 = Screen()
screen1.title("US. States games")
image = "blank_states_img.gif"
screen1.addshape(image)
shape(image)
screen1.tracer(0)

list_turtle = []
list_correct = []

data = read_csv('50_states.csv')
data_state = data["state"]
data_postion_x = data["x"].to_dict()
data_postion_y = data["y"]
copy_data_state = data_state

game_is_on = True
score = 0

while game_is_on:
    answer_state = screen1.textinput(title=f'{score}/50', prompt='Nhập tên tiểu bang:')
    if answer_state.title() == 'Exit':
        game_is_on = False
        screen1.bye()
    if (len(copy_data_state[data["state"] == answer_state.title()])) == 1:
        if not answer_state.title() in list_correct:
            turtle = Turtle()
            list_turtle.append(turtle)
            list_turtle[len(list_turtle) - 1].penup()
            list_turtle[len(list_turtle) - 1].hideturtle()
            pos_x = data_postion_x[data.index[data["state"] == answer_state.title()].tolist()[0]]
            pos_y = data_postion_y[data.index[data["state"] == answer_state.title()].tolist()[0]]
            list_turtle[len(list_turtle) - 1].goto(x=pos_x, y=pos_y)
            list_turtle[len(list_turtle) - 1].write(answer_state.title())
            screen1.update()
            list_correct.append(answer_state.title())
            score+=1
        else:
            print('Truc!')

###Đưa các states chưa đạt được vào trong 1 file csv
# states_not_find = []
# for i in copy_data_state.tolist():
#     if not i in list_correct:
#         states_not_find.append(i)

#Code nhanh hơn:
states_not_find = [state for state in copy_data_state.tolist() if not state in list_correct]

df_to_export = DataFrame(states_not_find)
df_to_export.to_csv('learn.csv')







#screen1.exitonclick()
#screen1.mainloop()

#Tìm hiểu thêm: Lấy các giá trị khi bấm chuột trên màn hình
