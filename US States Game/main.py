import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

usa = pd.read_csv("US States Game/50_states.csv")
state_list = []

for state in usa["state"]:
    state_list.append(state)

print(state_list)
score = 0

game_running = True
while game_running:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state in state_list:
        state = usa[usa["state"] == answer_state]

        x_cord = state["x"].item()
        y_cord = state["y"].item()

        t = turtle.Turtle()
        t.penup()
        t.goto(x_cord, y_cord)
        t.write(answer_state.upper(), font=("Arial", 6, "bold"))
        t.hideturtle()
        score += 1
    else:
        continue

screen.exitonclick()