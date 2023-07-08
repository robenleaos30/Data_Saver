import random
import pyperclip
import json
from tkinter import *
from tkinter import messagebox

# Find Password


def find_password():
    website = entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file in previous.")
    else:
        if website in data.keys():
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No data in the file.")

# Generate Password


def generate():
    entry2.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(4)]
    password_big_letter = [random.choice(big_letters) for _ in range(2)]
    password_symbol = [random.choice(symbols) for _ in range(2)]
    password_number = [random.choice(numbers) for _ in range(2)]

    password_list = password_number + password_letter + password_big_letter + password_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    entry2.insert(0, password)
    pyperclip.copy(password)

# Save


def save():
    website = entry.get()
    email = entry1.get()
    password = entry2.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as now_data:
            json.dump(data, now_data, indent=4)
    finally:
        entry.delete(0, END)
        entry2.delete(0, END)

# UI


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=1)

# text
text = Label(text="Website:")
text.grid(row=1, column=0)

text1 = Label(text="Email/Username:")
text1.grid(row=2, column=0)

text2 = Label(text="Password:")
text2.grid(row=3, column=0)

# entry
entry = Entry(width=17)
entry.grid(row=1, column=1)
entry.focus()

entry1 = Entry(width=35)
entry1.grid(row=2, column=1, columnspan=2)
entry1.insert(0, "aung@gmail.com")

entry2 = Entry(width=17)
entry2.grid(row=3, column=1, columnspan=1)

# button
button = Button(text="Generate Password", command=generate)
button.grid(row=3, column=2, columnspan=1)

button1 = Button(text="Add", width=30, command=save)
button1.grid(row=4, column=1, columnspan=2)

button2 = Button(text="Search", width=14, command=find_password)
button2.grid(row=1, column=2)

window.mainloop()
