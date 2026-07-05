from turtle import Turtle, Screen, heading
import random

tim = Turtle()
tim.pensize(2)
tim.speed(0)
screen = Screen()

# Square 
# for i in range(4):
#     tim.forward(200) 
#     tim.right(90)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         tim.color(c)
#         tim.forward(steps)
#         tim.right(30)

# for i in range(10):
#     tim.forward(10)

# 3 Sides
# tim.forward(200)
# tim.right(120)
# tim.forward(200)
# tim.right(120)
# tim.forward(200)
# tim.right(120)

# 4 Sides
# tim.forward(300)
# tim.right(90)
# tim.forward(300)
# tim.right(90)
# tim.forward(300)
# tim.right(90)
# tim.forward(300)
# tim.right(90)

# color = ["black","blue","yellow", "red"]

# for i in range(3,12):
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360/i)
#         tim.color(color[i%len(color)])

# colors = ["DeepSkyBlue2", "DeepSkyBlue3", "DeepSkyBlue4", 
# "DodgerBlue",
# "DodgerBlue1",
# "DodgerBlue2",
# "DodgerBlue3",
# "DodgerBlue4",
# "gold1",
# "gold2",
# "gold3",
# "gold4",
# "green",
# "green1",
# "green2",
# "green3",
# "green4",
# "ivory",
# "ivory1",
# "ivory2",
# "ivory3",
# "ivory4",
# "LightPink",
# "LightPink1",
# "LightPink2",
# "LightPink3",
# "LightPink4",
# ]

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)
    

def draw_spirograph(gap_size):

    original_heading = tim.heading()
        
    while True:
        tim.setheading(tim.heading() + gap_size)
        tim.pencolor(random_color())
        tim.circle(100)
        if original_heading == tim.heading():
            break

draw_spirograph(40)


screen.exitonclick()