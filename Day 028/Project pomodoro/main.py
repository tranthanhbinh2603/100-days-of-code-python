
from tkinter import *
from time import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
TITLE = "Timer"
START = "Start"
RESET = "Reset"


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title('Pomotoro')
windows.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

label_title = Label(text=TITLE, font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

button_start = Button(text=START, font=('Arial', 10))
button_start.grid(column=0, row=2)

button_check_mark = Button(text=CHECK_MARK, highlightthickness=0, fg=GREEN, bg=YELLOW)
button_check_mark.grid(column=1, row=3)

button_reset = Button(text=RESET, highlightthickness=0)
button_reset.grid(column=2, row=2)



windows.mainloop()