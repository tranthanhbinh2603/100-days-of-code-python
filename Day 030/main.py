from tkinter import *
from tkinter import messagebox
import random
#Sử dụng pypercilp
#import pyperclip
import json

WIDTH_ENTRY = 35

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def PasswordGen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for n in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for n in range(random.randint(2, 4))]
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # Dùng join
    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(string=password,index=0)
    #pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if entry_website.get() == "":
        messagebox.showinfo(title="Error", message="The website is not empty")
        return
    if entry_username.get() == "":
        messagebox.showinfo(title="Error", message="The username is not empty")
        return
    if entry_password.get() == "":
        messagebox.showinfo(title="Error", message="The password is not empty")
        return
    if (messagebox.askokcancel(title="Conform", message="Do you save?\nThis is not undo")):
        new_data = {
            entry_website.get():
                {
                    "username": entry_username.get(),
                    "password": entry_password.get()
                }
        }
        # Ghi file json
        # with open('data.json', mode='w') as f:
        #     json.dump(new_data, f, indent=4)
        #     entry_website.delete(0, END)
        #     entry_password.delete(0, END)

        try:
            #Update file json:
            with open('data.json', mode='r') as f:
                data = json.load(f)
                data.update(new_data)
            with open('data.json', mode='w') as f:
                json.dump(data, f, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', mode='w') as f:
                json.dump(new_data, f, indent=4)
        except FileNotFoundError:
            with open('data.json', mode='w') as f:
                json.dump(new_data, f, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

        #Đọc file json
        # with open('data.json', mode='r') as f:
        #     data = json.load(f)
        #     print(data)

# ---------------------------- SEARCH   ------------------------------- #
def find_password():
    try:
        with open('data.json', mode='r') as f:
            if str(entry_website.get()) in json.load(f):
                with open('data.json', mode='r') as f:
                    data = json.load(f)
                    username = data[str(entry_website.get())]['username']
                    password = data[str(entry_website.get())]['password']
                    messagebox.showinfo(title="Info", message=f"User name: {username}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error", message="No detail for website exist")
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No find file error')


# ---------------------------- UI SETUP ------------------------------- #
scrren = Tk()
scrren.config(pady=20, padx=20)
scrren.title('Password Manager')

#Link đến Tkter về canvas: https://tkdocs.com/tutorial/canvas.html
canvas_logo = Canvas(width=200, height=200)
image_logo = PhotoImage(file='logo.png')
canvas_logo.create_image(300, 100, image=image_logo)
canvas_logo.grid(column=1, row=0)

#Xem về column span: https://replit.com/@appbrewery/grid-columnspan-demo#main.py

label_website = Label(text='Website:')
label_website.grid(row=1, column=0)

label_username = Label(text='Email/Username:')
label_username.grid(row=2, column=0)

label_password = Label(text='Password:')
label_password.grid(row=3, column=0)

entry_website = Entry(width=21)
entry_website.grid(row=1, column=1, sticky="W")
#entry_website.insert(string="google.com", index=0)

entry_username = Entry(width=WIDTH_ENTRY)
entry_username.grid(row=2, column=1, columnspan=2)
#entry_username.insert(string="tranthanhbinh@gmail.com", index=0) #Mới, dùng để test

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky="W") #Mới nha
#entry_password.insert(string="1234", index=0)

button_gen = Button(text="Generate Password", width=14, command=PasswordGen)
button_gen.grid(row=3, column=2)

button_add = Button(text="Add", width=WIDTH_ENTRY, command=save)
button_add.grid(row=4, column=1, columnspan=2)

button_sea = Button(text="Search", width=14, command=find_password)
button_sea.grid(row=1, column=2)


scrren.mainloop()