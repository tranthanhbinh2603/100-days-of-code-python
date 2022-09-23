from tkinter import *

windows = Tk()
windows.title('LEARNING')
windows.config(padx=100, pady=50, bg="#f7f5dd")

#Canvas trong tkinter:
canvas = Canvas(width=200, height=224, bg="#f7f5dd",highlightthickness=0) #Khong co highlightthickness thì nó sẽ có viền nhé
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 112, text="00:00", fill='white', font=('time new roman', 20))
canvas.pack()

windows.mainloop()

#Có thể chọn màu tại: https://colorhunt.co/

