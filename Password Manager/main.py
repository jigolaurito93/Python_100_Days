from email import message
from tkinter import *
from tkinter import messagebox
import pyperclip

FONT = ("Arial", 12, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():

    password_textbox.delete(0, END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_', '=', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '<', '>']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_textbox.insert(END, string=password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_textbox.get()
    email = email_textbox.get()
    password = password_textbox.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
        return

    is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email} \nPassword: {password} \n\nIs it okay to save?")

    if is_okay:
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
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky="e", pady=(0,5))
submit_btn = Button(text="Add", width=36, command=save)
submit_btn.grid(column=1, row=4, columnspan=2, sticky="ew")




window.mainloop()