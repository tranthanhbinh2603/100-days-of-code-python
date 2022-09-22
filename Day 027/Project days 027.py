from tkinter import *
from tkinter.ttk import *

#TODO 0: Create scrren
scrren = Tk()
scrren.minsize(width=200, height=100)
scrren.config(padx=20, pady=20)
scrren.title('Mile to Km Converter')

#TODO 2: Create func caculator:
def caculator():
    answer['text'] = float(entry_miles.get()) * 1.6

#TODO 1: Create label, entry and button

text_equal = "is equal to"
text_miles = "Miles"
text_km = "Km"
text_number_start = 0
text_caculate = "Calculate"

#TODO 1a: Label
label_equal = Label(scrren, text=text_equal)
label_equal.grid(column=0, row=1)

label_miles = Label(scrren, text=text_miles)
label_miles.grid(column=2, row=0)

entry_miles = Entry()
entry_miles.insert(END, string=str(text_number_start))
entry_miles.config(width=10)
entry_miles.grid(column=1, row=0)

answer = Label(scrren, text=str(text_number_start))
answer.grid(column=1, row=1)

label_km = Label(scrren, text=text_km)
label_km.grid(column=2, row=1)

button_run = Button(text=text_caculate, command=caculator)
button_run.grid(column=1, row=2)






scrren.mainloop()
