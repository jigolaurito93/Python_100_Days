from turtle import Turtle
import random
import time


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        # self.goto(310, random.randint(-210,260))
        self.goto(310, -200)
        self.setheading(180)
    
    def drive(self):
        self.forward(10)
