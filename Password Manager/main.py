from tkinter import *
from turtle import width

FONT = ("Arial", 12, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_textbox.get()
    email = email_textbox.get()
    password = password_textbox.get()

    with open("Password Manager/data.txt", mode="a") as pw_data:
        pw_data.write(f"{website} | {email} | {password} \n")
    
    website_textbox.delete(0, END)
    email_textbox.delete(0, END)
    password_textbox.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
pw_logo = PhotoImage(file="Password Manager/logo.png")
canvas.create_image(100, 100, image=pw_logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, padx=(0,5), sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, padx=(0,5), sticky="e")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, padx=(0,5), sticky="e")

# Textbox
website_textbox = Entry(width=35)
website_textbox.grid(column=1, row=1, columnspan=2, sticky="ew", pady=(0,5))
website_textbox.focus()
email_textbox = Entry(width=35)
email_textbox.grid(column=1, row=2, columnspan=2, sticky="ew", pady=(0,5))
password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3, sticky="ew", padx=(0, 5), pady=(0,5))

# Buttons
generate_password_btn = Button(text="Generate Password")
generate_password_btn.grid(column=2, row=3, sticky="e", pady=(0,5))
submit_btn = Button(text="Add", width=36, command=save)
submit_btn.grid(column=1, row=4, columnspan=2, sticky="ew")




window.mainloop()