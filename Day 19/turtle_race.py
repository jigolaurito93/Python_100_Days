from turtle import Turtle, Screen
import random

screen = Screen()
choice = screen.textinput("Turtle Race", "Make your bet on a turtle color: red, blue, green, yellow, orange: ")
screen.screensize(500, 500)

t_line = Turtle()
t_line.hideturtle() # Hides the arrow icon so only text/stamps show
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
    t[i].shape("turtle") 
    t[i].color(colors[i]) 
    t[i].penup() 
    t[i].goto(-230, 100 - (i * 50)) 

game_over = False
while not game_over:
    for i in range(5):
        t[i].forward(random.randint(1, 10)) # Increased speed slightly for a faster race
        
        if t[i].xcor() >= 200:
            winner_color = colors[i].title()
            
            # 1. Determine the result message string
            if colors[i] == choice.lower():
                result_msg = f"{winner_color} wins! You win!"
            else:
                result_msg = f"{winner_color} wins! You lose!"
                
            # Print to console (keeping your original logic)
            print(f"{winner_color} turtle wins!")
            print("You win!" if colors[i] == choice.lower() else "You lose!")
            
            game_over = True
            
            # 2. Display "Game Over" on screen
            t_line.penup()
            t_line.goto(0, 50) # Moves it up so it does not overlap the winner message
            t_line.write(
                "Game Over", 
                align="center", 
                font=("Verdana", 30, "bold")
            )
            
            # 3. Display the Winner Announcement on screen
            t_line.goto(0, -10) # Move slightly down below "Game Over"
            t_line.write(
                result_msg, 
                align="center", 
                font=("Verdana", 20, "normal")
            )
            break # Exit the loop immediately once a winner is found

screen.exitonclick()
