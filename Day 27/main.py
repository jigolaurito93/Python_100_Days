import tkinter

window = tkinter.Tk()
window.title("This is the title")
window.minsize(width=500, height=600)
window.config(padx=200, pady=100)

my_label = tkinter.Label(text="This is a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=20, y=300)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)




def button_clicked():
    # new_text = input.get()
    my_label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

button2 = tkinter.Button(text="Click me also!")
button2.grid(column=2, row=0)

input = tkinter.Entry()
input.grid(column=3, row=2)

# input.pack()

# print(input.get())









window.mainloop()