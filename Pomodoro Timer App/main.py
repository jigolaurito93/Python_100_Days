from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_ICON = "🍅"
BREAK_ICON = "☕"
REP = 1
TIMER = 1
ICONS = []

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global TIMER, ICONS, REP

    if TIMER is not None and TIMER != 1:
        window.after_cancel(TIMER)

    TIMER = 1
    REP = 1


    canvas.itemconfig(timer_text, text="00:00", fill="white")
    timer_label.config(text="Timer", fg=GREEN)
    for label in ICONS:
        label.destroy()
    ICONS = []

    for i in range(7):
        if i % 2 == 0:
            check_mark = Label(text=TOMATO_ICON, fg=RED, bg=YELLOW, font=("Courier", 30))
            ICONS.append(check_mark)
        elif i % 2 == 1:
            check_mark = Label(text=BREAK_ICON, bg=YELLOW, font=("Courier", 26))
            ICONS.append(check_mark)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REP, TIMER   

    if TIMER is None:
        return

    # WORK MINUTES
    if REP in (1, 3, 5):
            timer_label["text"] = "Timer"
            timer_label["fg"] = GREEN
            ICONS[REP-1].place(x=(REP-1)*80 + 22, y=400)
            canvas.itemconfig(timer_text, fill="white")
            count_down(60 * WORK_MIN)

    # SHORT BREAK
    elif REP in (2, 4):
            timer_label["text"] = "Break"
            timer_label["fg"] = PINK
            ICONS[REP-1].place(x=(REP-1)*80 + 15, y=400)
            canvas.itemconfig(timer_text, fill="#2ecc71")

    # LONG BREAK
    elif REP == 6:
            timer_label["text"] = "Break"
            ICONS[REP-1].place(x=(REP-1)*80 + 22, y=400)
            count_down(60 * LONG_BREAK_MIN)

    elif REP == 0:
        REP = 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global REP, TIMER
    minutes = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1 )
    elif count == 0:
        REP += 1
        TIMER = window.after(1000, start_timer)

def display_icon():
    pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer App")
window.config(padx=100, pady=120, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro Timer App/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Timer Text
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(
    text="Start",
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
    height=2,
    command=reset_timer)
reset_btn.grid(column=2, row=2)



for i in range(7):
    if i % 2 == 0:
       check_mark = Label(text=TOMATO_ICON, fg=RED, bg=YELLOW, font=("Courier", 30))
       ICONS.append(check_mark)
    elif i % 2 == 1:
        check_mark = Label(text=BREAK_ICON, bg=YELLOW, font=("Courier", 26))
        ICONS.append(check_mark)

window.mainloop()