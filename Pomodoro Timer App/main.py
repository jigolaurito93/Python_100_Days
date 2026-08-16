from ast import Global
from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK_ICON = "✔"
BREAK_ICON = "☕"
REP = 1


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REP

    # WORK MINUTES
    if REP in (1, 3, 5):
            icons[REP-1].place(x=(REP-1)*40 + 10, y=350)
            canvas.itemconfig(timer_text, fill="white")
            count_down(3)
    # SHORT BREAK
    elif REP in (2, 4):
            icons[REP-1].place(x=(REP-1)*40 + 3, y=350)
            canvas.itemconfig(timer_text, fill="#2ecc71")
            count_down(5)
    # LONG BREAK
    elif REP == 6:
            icons[REP-1].place(x=(REP-1)*40 + 10, y=350)
            count_down(6)

    # # WORK MINUTES
    # if REP in (1, 3, 5):
    #         count_down(60 * WORK_MIN)
    # # SHORT BREAK
    # elif REP in (2, 4,):
    #         count_down(60 * SHORT_BREAK_MIN)
    # # LONG BREAK
    # elif REP == 6:
    #         count_down(60 * LONG_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
seconds=0

def count_down(count):
    global REP
    minutes = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    
    if count > 0:
        window.after(1000, count_down, count - 1 )
    elif count == 0:
        REP += 1
        window.after(1000, start_timer)

def display_icon():
    pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer App")
window.config(padx=100, pady=120, bg=YELLOW)



timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro Timer App/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Timer Text
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(
    text="Start Break",
    font=("Arial", 14, "bold"), 
    fg="white", 
    bg="#2ecc71", 
    activeforeground="white", 
    activebackground="#27ae60", 
    highlightthickness=0, 
    relief="ridge", 
    bd=0, 
    width=12,
    height=2,
    command=start_timer)

start_btn.grid(column=0, row=2)

reset_btn = Button(
    text="Reset", 
    font=("Arial", 14, "bold"), 
    fg="white", 
    bg="#2ecc71", 
    activeforeground="white", 
    activebackground="#27ae60", 
    highlightthickness=0, 
    relief="ridge", 
    bd=0, 
    width=12,
    height=2)
reset_btn.grid(column=2, row=2)

icons = []

for i in range(7):
    if i % 2 == 0:
       check_mark = Label(text=CHECK_MARK_ICON, fg=RED, bg=YELLOW, font=("Courier", 25))
       icons.append(check_mark)
    elif i % 2 == 1:
        check_mark = Label(text=BREAK_ICON, bg=YELLOW, font=("Courier", 25))
        icons.append(check_mark)






window.mainloop()