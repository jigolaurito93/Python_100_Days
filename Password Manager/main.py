from email import message
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

FONT = ("Arial", 12, "bold")
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def find_password():
    website = website_textbox.get().title()

    # NO DATA FILE FOUND
    try:
        with open("Password Manager/data.json", "r") as pw_data:
            data = json.load(pw_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
        return
    # NO DETAILS FOR THE WEBSITE
    else:
        try:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        except KeyError as error_message:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exist")
            return



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
    website = website_textbox.get().title()
    email = email_textbox.get()
    password = password_textbox.get()

    new_json_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
        return

    is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email} \nPassword: {password} \n\nIs it okay to save?")

    if is_okay:
        # If file exist, read the file and update with new json data
        try:
            with open("Password Manager/data.json", mode="r") as pw_data:
                # Read old data
                data = json.load(pw_data)

        # If file doesn't exist, create a new file
        except FileNotFoundError:
            with open("Password Manager/data.json", mode="w") as pw_data:
                data = json.dump(new_json_data, pw_data, indent=4)

        # If file does exist, add replace json file with new one
        else:
            # Save updated data
            data.update(new_json_data)
            with open("Password Manager/data.json", mode="w") as pw_data:
                json.dump(data, pw_data, indent=4)
        finally:
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
website_textbox = Entry(width=21)
website_textbox.grid(column=1, row=1, sticky="ew", padx=(0, 5), pady=(0,5))
website_textbox.focus()
email_textbox = Entry(width=35)
email_textbox.grid(column=1, row=2, columnspan=2, sticky="ew", pady=(0,5))
password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3, sticky="ew", padx=(0, 5), pady=(0,5))

# Buttons
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="ew", pady=(0,5))
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky="e", pady=(0,5))
submit_btn = Button(text="Add", width=36, command=save)
submit_btn.grid(column=1, row=4, columnspan=2, sticky="ew")




window.mainloop()