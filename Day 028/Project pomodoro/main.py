
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
reps = 1
string_check_mark = "11111"
windows_after = NONE


# ---------------------------- TIMER RESET ------------------------------- # 
def Timer_reset():
    windows.after_cancel(windows_after)
    label_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global string_check_mark
    string_check_mark = ""
    global reps
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    #Chanlge:
    global reps
    global string_check_mark
    if reps == 8:
        label_title.config(text="Break", fg=RED)
        Count_down(LONG_BREAK_MIN * 60)
        string_check_mark += CHECK_MARK
        button_check_mark.config(text=string_check_mark)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
        Count_down(SHORT_BREAK_MIN * 60)
        string_check_mark += CHECK_MARK
        button_check_mark.config(text=string_check_mark)
    else:
        label_title.config(text="Work", fg=GREEN)
        Count_down(WORK_MIN * 60)
    #Count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def Count_down(time):
    #Ở đây mình lấy thời gian hơi khác so với bản gốc:
    minute = str(round((time - (time % 60)) / 60)) #minute = math.floor(time/60)
    second = str(time % 60)
    if int(minute) < 10:
        minute = "0" + minute
    if int(second) < 10:
        second = "0" + second
    canvas.itemconfig(timer_text, text=minute  + ":" + second)
    if time > 0:
        global windows_after
        windows_after = windows.after(1000, Count_down, time-1)
    else:
        global reps
        reps += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title('Pomotoro')
windows.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

label_title = Label(text=TITLE, font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

button_start = Button(text=START, font=('Arial', 10), command=start_timer)
button_start.grid(column=0, row=2)

#button_check_mark = Label(text=CHECK_MARK, highlightthickness=0, fg=GREEN, bg=YELLOW)
button_check_mark = Label(highlightthickness=0, fg=GREEN, bg=YELLOW, font=('bold'))
button_check_mark.grid(column=1, row=3)

button_reset = Button(text=RESET, highlightthickness=0, command=Timer_reset)
button_reset.grid(column=2, row=2)

windows.mainloop()