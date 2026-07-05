import random
from turtle import Turtle, Screen, color

t = Turtle()
t.hideturtle()
screen = Screen()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def dot_row():
    for _ in range(10):
        color_choice = random_color()
        t.color(color_choice)
        t.dot(20, color_choice)
        t.forward(50)

y_pos = -225
for i in range(10):
    t.penup()
    t.goto(-225, y_pos)
    dot_row()
    y_pos += 50

screen.exitonclick()
