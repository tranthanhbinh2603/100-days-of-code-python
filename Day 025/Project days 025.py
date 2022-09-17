#https://www.sporcle.com/games/g/states
from turtle import *
from pandas import *

screen1 = Screen()
screen1.title("US. States games")
image = "blank_states_img.gif"
screen1.addshape(image)
shape(image)

data = read_csv('50_states.csv')
data_state = data["state"]
copy_data_state = data_state

game_is_on = True

while game_is_on:
    answer_state = screen1.textinput(title='Đoán đi', prompt='Nhập tên tiểu bang:')
    print(len(copy_data_state[data["state"] == answer_state.title()]))








#screen1.exitonclick()
screen1.mainloop()

#Tìm hiểu thêm: Lấy các giá trị khi bấm chuột trên màn hình
