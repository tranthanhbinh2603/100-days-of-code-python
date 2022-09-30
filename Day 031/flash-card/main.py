#--------------------------IMPORT-------------------------------#
from tkinter import *
from pandas import *
from random import *

#------------------FUNCTIONS--------------------------------#
def wrong():
    global windows_after
    scrren.after_cancel(windows_after)
    global data_learn
    data_learn= data[randint(0, len(data) - 1)]
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=data_learn['French'])
    canvas.itemconfig(image_canvas, image=image_front)
    windows_after = scrren.after(3000, change_image)

def right():
    global data_learn
    data.remove(data_learn)
    df = DataFrame(data)
    df.to_csv('data/words_to_learn.csv', index=False)
    #Thêm quả tính năng xoá bỏ từ trong danh sách và nạp lại:
    global windows_after
    scrren.after_cancel(windows_after)
    data_learn = data[randint(0, len(data) - 1)]
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=data_learn['French'])
    canvas.itemconfig(image_canvas, image=image_front)
    windows_after = scrren.after(3000, change_image)
    #Khác cái khi nhấn nút false ở chổ mình xoá đi và nạp lại:


def change_image():
    global data_learn
    canvas.itemconfig(image_canvas, image=image_back)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=data_learn['English'])


#--------------------------UI-----------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
windows_after = NONE
choosed = 0
data_learn = NONE

#Read data from CSV:
try:
    data = read_csv("data/words_to_learn.csv").to_dict(orient="records") #Lưu từng hàng dưới dạng 1 dict. Toàn bộ bảng là 1 list
except FileNotFoundError:
    data = read_csv("data/french_words.csv").to_dict(orient="records")
    data_frime = read_csv("data/french_words.csv")
    data_frime.to_csv('data/words_to_learn.csv', index=False)


scrren = Tk()
scrren.configure(bg=BACKGROUND_COLOR)
scrren.config(padx=50, pady=50)

#Card_Front
canvas = Canvas(height=526, width=800)
image_front = PhotoImage(file='images/card_front.png')
image_back = PhotoImage(file='images/card_back.png') #Khong dat chung vao ham
image_canvas = canvas.create_image(400, 263, image=image_front) #Để căn giữa cần chia đôi canvas
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) #Thêm dòng này xoá bỏ vùng trắng
language_text = canvas.create_text(400, 150, text="Franch", font=FONT_LANGUAGE)
data_learn = data[randint(0, len(data) - 1)]
word_text = canvas.create_text(400, 263, text=data_learn['French'], font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)

#Right
my_image_right = PhotoImage(file="images/right.png")
button_right = Button(image=my_image_right, highlightthickness=0, command=right)
button_right.grid(row=1,column=0)

#Wrong:
my_image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=my_image_wrong, highlightthickness=0, command=wrong)
button_wrong.grid(row=1,column=1)

windows_after = scrren.after(3000, change_image)

scrren.mainloop()