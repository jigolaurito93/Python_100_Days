from turtle import Turtle
import turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_COLOR = 'black'

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(TURTLE_COLOR)
        self.setheading(90)
        self.shape('turtle')
        self.goto(0, -270)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset(self):
        self.goto(STARTING_POSITION)

    # def move(self, x=0, y=0):
    #     self.forward(MOVE_DISTANCE)