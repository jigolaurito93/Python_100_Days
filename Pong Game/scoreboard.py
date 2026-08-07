from turtle import Turtle
FONT = ("Arial", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        if position == "left":
            self.goto(-150, 200)
        if position == "right":
            self.goto(150, 200)
        self.position = position
        self.write(self.score, align=self.position, font=FONT)
        
    
    def add_point(self):
        self.clear()
        self.score += 1
        self.write(self.score, align=self.position, font=FONT)
