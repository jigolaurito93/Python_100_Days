import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_label = turtle.Turtle()
state_label.penup()
state_label.hideturtle()


game_running = True
states = pandas.read_csv("US States Game/50_states.csv")

state_list = states["state"].to_list()
print(state_list)

score = 0
while game_running:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in states["state"].to_list():
        state = states.loc[states["state"] == answer_state]
        score += 1
        state_x_cor = state["x"].item()
        state_y_cor = state["y"].item()
        state_label.goto(state_x_cor, state_y_cor)
        state_label.write(answer_state, font=("Arial", 8, "normal"))





screen.exitonclick()