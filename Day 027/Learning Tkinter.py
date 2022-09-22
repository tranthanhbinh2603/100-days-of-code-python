#Tkinter: Là 1 bộ công cụ giúp tạo ra các GUI

from tkinter import *

screen = Tk()
screen.minsize(200,200)
screen.config(padx=20, pady=20)

#Tạo ra 1 label
label = Label(text="Hello")
label.pack()
label2 = Label(text="AAAAAA", font=('Arial', 20, 'italic'))
label2.pack(side='left')
label2["text"] = "ZZZZZ"
label.config(text="Hello!")

#Tạo ra 1 button
def Clicked():
    #print('I clicked')
    label['text'] = "I click button"
button1 = Button(text="Hello", command=Clicked)
button1.pack()

#Tạo textbox:
def Click_get_input():
    label['text'] = textbox1.get()
textbox1 = Entry()
textbox1.pack()
button2 = Button(text="Get value in entry", command=Click_get_input)
button2.pack()
button2.config(pady=20, padx=20)

#Một số cái khác:
#Xem file tkinter-widget-demo.py


#Các cách đặt vị trí -  Layout Managers
#Pack: ở trên
#Place: ở 1 vị trí nào đó
textbox3 = Entry()
textbox3.place(x=0, y=100)
#Grid: 1 hệ thống lưới
textbox4 = Entry()
#textbox4.grid(column=0, row=0) #Không dùng cùng với pack.








screen.mainloop()