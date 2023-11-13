import tkinter as tk
import random, string
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Password generator")
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=50, weight=1)

# image
logo = Image.open("images.png")
logo = ImageTk.PhotoImage(logo)
tk.Label(image=logo).grid(column=0, row=0)


def length_value(value):
    scale_value.set(int(value))


def generate_password():
    length = int(scale_value.get())
    characters = ""

    if numbers.get():
        characters += string.digits
    if capital_letters.get():
        characters += string.ascii_uppercase
    if lowercase.get():
        characters += string.ascii_lowercase
    if symbol.get():
        characters += string.punctuation

    password = []

    if not characters:
        label_password["text"] = f"Select at least one character"

    if length == 0:
        label_password["text"] = f"Select the password length"

    if characters:

        while length != 0:
            password.extend(random.choice(characters))
            length -= 1

        password = "".join(password)

        new_password = ''
        for element in password:
            new_password += "*"

        label_password["text"] = f"{new_password}"

        if show_password.get():
            label_password["text"] = f"{password}"


# length password
tk.Label(window, text="Choose the length of your password", font=("Arial", 13)).grid(row=0, column=1)
scale_value = IntVar()
scale = (Scale(window, from_=0, to=100, orient=HORIZONTAL, font=("Arial", 13), sliderlength=20, variable=scale_value))
scale.grid(row=0, column=2)

# instruction
tk.Label(window, text="What characters would you like to use for your password?\n"
                      "Select one of the following options:", font=("Arial", 13)).grid(row=2, column=1)

numbers = IntVar()
Checkbutton(window, text='Numbers', variable=numbers, font=("Arial", 13)).grid(column=0, row=3)

capital_letters = IntVar()
Checkbutton(window, text='Capital letters', variable=capital_letters, font=("Arial", 13)).grid(column=1, row=4)

lowercase = IntVar()
Checkbutton(window, text='Lowercase', variable=lowercase, font=("Arial", 13)).grid(column=1, row=3)

symbol = IntVar()
Checkbutton(window, text='Symbol', variable=symbol, font=("Arial", 13)).grid(column=3, row=3)

label_password = (tk.Label(master=window, text='Press "Generator password" to create the password\n'
                                               '\nSelect show password to display it!', font=("Arial", 15)))
label_password.grid(row=8, column=1)

Button(window, text="Generate password", font=("Arial", 13), command=generate_password, background="light grey").grid(
    row=6, column=1, sticky="nsew")
show_password = IntVar()
Checkbutton(window, text="Show password", variable=show_password, font=("Arial", 13)).grid(row=6, column=0)

window.mainloop()