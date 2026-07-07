from turtle import Turtle, Screen
import random


screen = Screen()
choice = screen.textinput("Turtle Race", "Make your bet on a turtle color: red, blue, green, yellow, orange: ")
screen.screensize(500, 500)


t_line = Turtle()
t_line.shape("square")
t_line.shapesize(stretch_wid=1, stretch_len=1)


left=410
right=390
for i in range(25):
    t_line.penup()
    t_line.goto(200, left)
    t_line.stamp()
    left-=40
for i in range(25):
    t_line.penup()
    t_line.goto(220, right)
    t_line.stamp()
    right-=40



t = []
for _ in range(5):
    t.append(Turtle())

colors = ["red", "blue", "green", "yellow", "orange"]

for i in range(5):
    t[i].shape("turtle") # assigns the shape
    t[i].color(colors[i]) # assigns the color
    t[i].penup() # lifts the pen
    t[i].goto(-230, 100 - (i * 50)) # assigns the position of each turtle

game_over = False
while not game_over:
    for i in range(5):
        t[i].forward(random.randint(1, 5))
        if t[i].xcor() >= 200:
            print(f"{colors[i].title()} turtle wins!")
            if colors[i] == choice.lower():
                print("You win!")
            else:
                print("You lose!")
            game_over = True   
            



screen.exitonclick()