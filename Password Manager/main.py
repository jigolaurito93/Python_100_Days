from tkinter import *
from turtle import width

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=220, height=220)
canvas = Canvas()
pw_logo = PhotoImage(file="Password Manager/logo.png")
canvas.create_image(200, 150, image=pw_logo)

canvas.pack(padx=50, pady=80)


window.mainloop()