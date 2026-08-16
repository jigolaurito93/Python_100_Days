from tkinter import *
from turtle import width

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=25, pady=25)

def convert_m_to_km():
    miles = input.get()
    km_value['text'] = round(float(miles) * 1.609344, 4)


input = Entry(width=7, font=("Arial", 12, "normal"))
input.grid(column=1, row=0)
input.insert(END, 0)

miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=("Arial", 12, "normal"))
equal_to_label.grid(column=0, row=1)

km_value = Label(text=0, font=("Arial", 12, "normal"))
km_value.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert_m_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()