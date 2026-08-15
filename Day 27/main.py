import tkinter

window = tkinter.Tk()
window.title("This is the title")
window.minsize(width=500, height=600)

my_label = tkinter.Label(text="This is a Label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()