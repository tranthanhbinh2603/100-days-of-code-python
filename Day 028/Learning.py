from tkinter import *

windows = Tk()
windows.title('LEARNING')

#Canvas trong tkinter:
canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()

windows.mainloop()
