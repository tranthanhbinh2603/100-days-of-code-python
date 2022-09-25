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

#Hàm after và đệ quy
def Recustion(thing):
    #Do some thing ......
    print(thing)
    windows.after(1000, Recustion, thing - 1)

Recustion(3)
windows.mainloop()

#Dynamic Typing:
dynamic = 0
if dynamic == 0:
    dynamic = "00"
print(dynamic) #Có tính đa biến, thay đổi kiểu dữ liệu liên tục

#Ngoài ra còn cái này dị hơn:
dynamic2 = 8
if dynamic2 < 10:
    dynamic2 = f"0{dynamic2}"
print(dynamic2)
#Đọc thêm: https://stackoverflow.com/questions/11328920/is-python-strongly-typed

#Hàm after cancel:
# timer = windows.after(1000, #Dosomething)
# windows.after_cancel(timer)


#Có thể chọn màu tại: https://colorhunt.co/

