#Tkinter: Là 1 bộ công cụ giúp tạo ra các GUI

from tkinter import *

screen = Tk()
screen.minsize(200,200)

label = Label(text="Hello")
label.pack()
label2 = Label(text="AAAAAA", font=('Arial', 20, 'italic'))
label2.pack(side='left')





screen.mainloop()